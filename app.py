from flask import Flask, request
from flask_restful import Api, Resource
import json
import pandas as pd

from pyspark.ml.recommendation import ALSModel
from pyspark.sql import Row
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext

# Create the application instance
app = Flask(__name__)
api = Api(app)

sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

model2 = ALSModel.load("NoteBooks/model")

lines = spark.read.text("Dataset/datasetFinalForALS.csv").rdd
parts = lines.map(lambda row: row.value.split(" "))
ratingsRDD = parts.map(
    lambda p: Row(userId=int(p[0]), restoId=int(p[1]), rating=float(p[2]), timestamp=float(p[3])))
ratings = spark.createDataFrame(ratingsRDD)

def getUserRecommend(userid):
    #typo = ratings.select("userId").distinct().filter(ratings.userId==int(userid))
    l = [{'userId': userid}]
    df = pd.DataFrame(l)
    typo = spark.createDataFrame(df)
    test = model2.recommendForUserSubset(typo,10)
    data = test.toPandas()
    return json.loads(data.to_json(indent=2))

class RestoRec(Resource):
    def get(self):
        y = json.loads(request.data)
        return getUserRecommend(y["userId"])

    def post(self):
        return {"data":"posted"}

api.add_resource(RestoRec,"/restrec_for_user")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

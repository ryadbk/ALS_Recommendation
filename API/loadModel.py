
from pyspark.ml.recommendation import ALSModel
from pyspark.sql import Row
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext
import json


if __name__ == '__main__':
    print("dflnfndfldnfklndlfkndankjlfn iuehjQAFIUJH IQEHfiuQEHFNILUJBNAFilb iahbsfbaf ")

sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

model2 = ALSModel.load("../NoteBooks/model/")

lines = spark.read.text("../Dataset/datasetFinalForALS.csv").rdd
parts = lines.map(lambda row: row.value.split(" "))
ratingsRDD = parts.map(
    lambda p: Row(userId=int(p[0]), restoId=int(p[1]), rating=float(p[2]), timestamp=float(p[3])))
ratings = spark.createDataFrame(ratingsRDD)

def getUserRecommend(userid):
    typo = ratings.select("userId").distinct().filter(ratings.userId==userid)
    test = model2.recommendForUserSubset(typo,10)
    data = json.dumps(test.collect())
    print(data)
    return data

def stopSparkSession():
    spark.stop()

getUserRecommend(2088)
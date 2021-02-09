#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS

from pyspark.sql import Row
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext


# In[2]:


#SparkSession init
sc = SparkContext.getOrCreate()
spark = SparkSession(sc)


# In[10]:


#laod dataset
lines = spark.read.text("Dataset/test.csv").rdd
#rdd = spark.sparkContext.parallelize(lines)
lines


# In[5]:


parts = lines.map(lambda row: row.value.split(" "))
ratingsRDD = parts.map(lambda p: Row(userId=int(p[0]), restoId=int(p[1]),rating=float(p[2]), timestamp=float(p[3])))


# In[7]:


ratings = spark.createDataFrame(ratingsRDD)


# In[ ]:


(training, test) = ratings.randomSplit([0.8, 0.2])
print(training.collect())
print(test.collect())

# Build the recommendation model using ALS on the training data
# Note we set cold start strategy to 'drop' to ensure we don't get NaN evaluation metrics
# In[8]:


als = ALS(maxIter=5, regParam=0.01, userCol="userId",
          itemCol="restoId", ratingCol="rating",
          coldStartStrategy="drop")
model = als.fit(training)


# ### Evaluate the model by computing the RMSE on the test data

# In[9]:


predictions = model.transform(test)
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
                                predictionCol="prediction")
rmse = evaluator.evaluate(predictions)


# In[10]:


print("Root-mean-square error = " + str(rmse))


# In[11]:


# meilleurs 10 resto recommendees pour chaque user
userRecs = model.recommendForAllUsers(10)
# meilleurs 10 user recommendees pour chaque resto
movieRecs = model.recommendForAllItems(10)
print(userRecs.collect())

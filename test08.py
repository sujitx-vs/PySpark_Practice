from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RDD Demo").getOrCreate()

sc = spark.sparkContext

numbers = [1,2,3,4,5]

rdd = sc.parallelize(numbers)

print(type(rdd))

spark.stop()
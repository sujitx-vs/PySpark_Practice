from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("My First Spark App").getOrCreate()

print("Spark Started Successfully!")

print(type(spark))

spark.stop()

print("After spark.stop()")
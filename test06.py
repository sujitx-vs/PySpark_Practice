from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark Context Demo").getOrCreate()

print(type(spark))
print(type(spark.sparkContext))

spark.stop()
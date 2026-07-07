from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkContext Demo").getOrCreate()

sc = spark.sparkContext

print(sc)

spark.stop()
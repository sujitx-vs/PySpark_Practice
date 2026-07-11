from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("External Dataset").getOrCreate()

sc = spark.sparkContext

rdd = sc.textFile("data/employees.txt")

print(type(rdd))
print(rdd.getNumPartitions())

print(rdd.collect())

spark.stop()
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read Text File").getOrCreate()

sc = spark.sparkContext

rdd = sc.textFile("data/employees.txt",4) # no. of partition hardcoded.

print("Type:", type(rdd))
print("Partitions:", rdd.getNumPartitions())
print("Data:", rdd.collect())

spark.stop()
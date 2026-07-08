from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Partitions Demo").getOrCreate()

sc = spark.sparkContext

numbers = list(range(1, 21))

rdd = sc.parallelize(numbers)

print("Number of partitions:", rdd.getNumPartitions())

spark.stop()
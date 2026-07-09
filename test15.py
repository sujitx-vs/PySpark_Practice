from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Take Action").getOrCreate()

sc = spark.sparkContext

numbers = list(range(1, 21))

rdd = sc.parallelize(numbers)

rdd = rdd.map(lambda x: x * 10)

print("First 5 elements:", rdd.take(5))

spark.stop()
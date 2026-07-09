from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Collect Action").getOrCreate()

sc = spark.sparkContext

numbers = [1, 2, 3, 4, 5]

rdd = sc.parallelize(numbers)

rdd = rdd.map(lambda x: x * 2)

print("Before collect()")

result = rdd.collect()

print("After collect()")

print(result)

spark.stop()
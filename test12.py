from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Lazy Evaluation").getOrCreate()

sc = spark.sparkContext

numbers = [1, 2, 3, 4, 5]

rdd = sc.parallelize(numbers)

print("Before map")

rdd = rdd.map(lambda x: x * 2)

print("After map")

spark.stop()
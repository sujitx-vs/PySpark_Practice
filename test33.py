from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Broadcast Demo").getOrCreate()

sc = spark.sparkContext

# Create an RDD
numbers = sc.parallelize([1, 2, 3, 4, 5])

# Normal Python variable
multiplier = 10

# Broadcast the variable
broadcast_multiplier = sc.broadcast(multiplier)

# Use the broadcast variable
result = numbers.map(lambda x: x * broadcast_multiplier.value)

print(result.collect())

spark.stop()
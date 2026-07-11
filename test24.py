from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Passing Functions").getOrCreate()

sc = spark.sparkContext

def square(x):
    return x * x

numbers = sc.parallelize([1, 2, 3, 4, 5])

result = numbers.map(square)

print(result.collect())

spark.stop()
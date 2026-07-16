from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Accumulator Demo").getOrCreate()

sc = spark.sparkContext

numbers = sc.parallelize([1, 2, 3, 4, 5])

# Create accumulator
total = sc.accumulator(0)

def add_number(x):
    global total
    total += x

numbers.foreach(add_number)

print("Sum:", total.value)

spark.stop()
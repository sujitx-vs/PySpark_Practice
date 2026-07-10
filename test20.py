from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Reduce Demo").getOrCreate()

sc = spark.sparkContext

numbers = [10, 20, 30, 40]

rdd = sc.parallelize(numbers)

total = rdd.reduce(lambda a, b: a + b)

print("Total:", total)

spark.stop()
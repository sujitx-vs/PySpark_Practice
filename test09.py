from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Parallelize Demo").getOrCreate()

sc = spark.sparkContext

numbers = [10, 20, 30, 40, 50]

rdd = sc.parallelize(numbers)

print(type(numbers))
print(type(rdd))

spark.stop()
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Filter Demo").getOrCreate()

sc = spark.sparkContext

numbers = [10, 25, 40, 55, 70, 85]

rdd = sc.parallelize(numbers)

filtered_rdd = rdd.filter(lambda x: x > 50)

print(filtered_rdd.take(10))

spark.stop()
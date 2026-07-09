from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Count Action").getOrCreate()

sc = spark.sparkContext

numbers = [10, 20, 30, 40, 50]

rdd = sc.parallelize(numbers)

rdd = rdd.map(lambda x: x * 2)

print("Count:", rdd.count())

spark.stop()

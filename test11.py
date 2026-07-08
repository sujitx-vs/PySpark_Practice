from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Transformations and Actions").getOrCreate()

sc = spark.sparkContext

numbers = [1, 2, 3, 4, 5]

rdd = sc.parallelize(numbers)

new_rdd = rdd.map(lambda x: x * 2)

print(type(new_rdd))

spark.stop()
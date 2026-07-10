from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReduceByKey Demo").getOrCreate()

sc = spark.sparkContext

data = [
    ("Apple", 2),
    ("Apple", 3),
    ("Banana", 5),
    ("Apple", 4),
    ("Banana", 1),
    ("Orange", 6)
]

rdd = sc.parallelize(data)

result = rdd.reduceByKey(lambda a, b: a + b)

print(result.collect())

spark.stop()
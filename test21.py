from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Key Value RDD").getOrCreate()

sc = spark.sparkContext

data = [
    ("Milk", 1),
    ("Bread", 1),
    ("Milk", 1),
    ("Rice", 1)
]

rdd = sc.parallelize(data)

print(rdd.collect())

spark.stop()
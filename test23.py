from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("GroupByKey Demo").getOrCreate()

sc = spark.sparkContext

data = [
    ("Apple", 2),
    ("Apple", 3),
    ("Banana", 5),
    ("Apple", 4),
    ("Banana", 1)
]

rdd = sc.parallelize(data)

grouped = rdd.groupByKey()

result = grouped.mapValues(list)

print(result.collect())

spark.stop()
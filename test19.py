from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Map vs FlatMap").getOrCreate()

sc = spark.sparkContext

sentences = [
    "I love Spark",
    "Spark is fast",
    "Big Data"
]

rdd = sc.parallelize(sentences)

mapped = rdd.map(lambda sentence: sentence.split(" "))

flatmapped = rdd.flatMap(lambda sentence: sentence.split(" "))

print("MAP:")
print(mapped.collect())

print()

print("FLATMAP:")
print(flatmapped.collect())

spark.stop()
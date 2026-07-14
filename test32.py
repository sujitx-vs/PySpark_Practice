from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RDD Unpersist Demo").getOrCreate()

sc = spark.sparkContext

rdd = sc.textFile("data/employees.txt")

upper_rdd = rdd.map(lambda x: x.upper())

upper_rdd.cache()

print("First Action:")
print(upper_rdd.collect())

# Remove cached data
upper_rdd.unpersist()

print("\nSecond Action:")
print("Count:", upper_rdd.count())

spark.stop()
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RDD Cache Demo").getOrCreate()

sc = spark.sparkContext

# Read external file
rdd = sc.textFile("data/employees.txt")

# Transformation
upper_rdd = rdd.map(lambda x: x.upper())

# Cache the transformed RDD
upper_rdd.cache()

print("First Action:")
print(upper_rdd.collect())

print("\nSecond Action:")
print("Total Records:", upper_rdd.count())

spark.stop()
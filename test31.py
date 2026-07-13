from pyspark.sql import SparkSession
from pyspark.storagelevel import StorageLevel

spark = SparkSession.builder.appName("RDD Persist Demo").getOrCreate()

sc = spark.sparkContext

rdd = sc.textFile("data/employees.txt")

upper_rdd = rdd.map(lambda x: x.upper())

# Persist using Memory + Disk
upper_rdd.persist(StorageLevel.MEMORY_AND_DISK)

print("Data:")
print(upper_rdd.collect())

print("\nCount:")
print(upper_rdd.count())

spark.stop()
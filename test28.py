from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read JSON as Text").getOrCreate()

sc = spark.sparkContext

rdd = sc.textFile("data/employees.json")

print("Type:", type(rdd))
print("Partitions:", rdd.getNumPartitions())
print("Data:")

for line in rdd.collect():
    print(line)

spark.stop()
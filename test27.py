from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read CSV as Text").getOrCreate()

sc = spark.sparkContext

rdd = sc.textFile("data/employees.csv")

print("Type:", type(rdd))
print("Partitions:", rdd.getNumPartitions())
print("Data:")

for line in rdd.collect():
    print(line)

spark.stop()
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read Multiple Files").getOrCreate()

sc = spark.sparkContext

# rdd = sc.textFile("data/*.txt")
rdd = sc.textFile("data/employees.txt,data/departments.txt")

print("Partitions:", rdd.getNumPartitions())
print("Data:")

for line in rdd.collect():
    print(line)

spark.stop()
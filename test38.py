from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.appName("DataFrame Viewing").getOrCreate()

# Sample Data
data = [
    ("Rahul", 25, 50000),
    ("Anu", 22, 60000),
    ("John", 30, 55000),
    ("Riya", 28, 70000)
]

# Create DataFrame
df = spark.createDataFrame(data, ["Name", "Age", "Salary"])

print("show()")
df.show()

print("\nhead()")
print(df.head())

print("\ntake(2)")
print(df.take(2))

print("\ncollect()")
print(df.collect())

spark.stop()
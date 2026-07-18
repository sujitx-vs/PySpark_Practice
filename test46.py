from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.appName("GroupBy Count").getOrCreate()

# Sample Data
data = [
    ("Rahul", "IT"),
    ("Anu", "HR"),
    ("John", "IT"),
    ("Riya", "HR"),
    ("David", "IT")
]

# Create DataFrame
df = spark.createDataFrame(
    data,
    ["Name", "Department"]
)

print("Original Data")
df.show()

print("Employee Count by Department")
df.groupBy("Department").count().show()

spark.stop()
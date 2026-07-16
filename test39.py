from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.appName("Select Columns").getOrCreate()

# Sample Data
data = [
    ("Rahul", 25, 50000),
    ("Anu", 22, 60000),
    ("John", 30, 55000),
    ("Riya", 28, 70000)
]

# Create DataFrame
df = spark.createDataFrame(
    data,
    ["Name", "Age", "Salary"]
)

print("Original DataFrame")
df.show()

print("\nOnly Name")
df.select("Name").show()

print("\nName and Salary")
df.select("Name", "Salary").show()

spark.stop()
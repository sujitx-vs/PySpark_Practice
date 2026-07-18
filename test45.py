from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.appName("Drop Column").getOrCreate()

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

# Drop Age column
df2 = df.drop("Age")

print("After Dropping Age")
df2.show()

spark.stop()
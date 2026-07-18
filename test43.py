from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.appName("Modify Column").getOrCreate()

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

print("Original Salary")
df.show()

# Increase salary by 10%
df2 = df.withColumn("Salary", df.Salary * 1.10)

print("Updated Salary")
df2.show()

spark.stop()
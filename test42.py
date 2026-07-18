from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.appName("withColumn Demo").getOrCreate()

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

print("Original Data")
df.show()

# Create a new column
df2 = df.withColumn("Bonus", df.Salary * 0.10)

print("After Adding Bonus")
df2.show()

spark.stop()
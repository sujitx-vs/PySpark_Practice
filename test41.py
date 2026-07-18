from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.appName("Where Demo").getOrCreate()

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

print("Salary > 55000")
df.where(df.Salary > 55000).show()

spark.stop()
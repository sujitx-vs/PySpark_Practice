from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.appName("Create DataFrame").getOrCreate()

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

# Display DataFrame
df.show()

spark.stop()
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Broadcast Lookup").getOrCreate()

sc = spark.sparkContext

# Employee IDs
employee_ids = sc.parallelize([101, 102, 103, 104])

# Small lookup table
employee_names = {
    101: "Rahul",
    102: "Anu",
    103: "John",
    104: "Priya"
}

# Broadcast the lookup table
broadcast_names = sc.broadcast(employee_names)

# Lookup names
result = employee_ids.map(
    lambda emp_id: (emp_id, broadcast_names.value[emp_id])
)

print(result.collect())

spark.stop()
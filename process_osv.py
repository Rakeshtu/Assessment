from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode

spark = SparkSession.builder \
    .appName("OSV Processing") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()


df = spark.read.json("/opt/airflow/data/osv_data.json")


df = df.select(
    col("vulns.id").alias("vulnerability_id"),
    col("vulns.aliases").alias("aliases"),
    explode(col("vulns.affected")).alias("affected_package"),
    col("vulns.modified").alias("modified_date")
)


df.write.format("delta").mode("overwrite").save("/mnt/delta/osv_data")

print("Processing completed successfully!")

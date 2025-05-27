from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WebLogAnalysis").getOrCreate()
df = spark.read.text("data/sample_logs.txt")
df.show(5)

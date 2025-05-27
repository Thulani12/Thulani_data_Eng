import pandas as pd

# Read sample data
df = pd.read_csv("data/sample_sales.csv")

# Clean data
df = df.dropna()
df["Date"] = pd.to_datetime(df["Date"])

# Aggregate totals
summary = df.groupby("Product").agg({"Quantity": "sum", "Total": "sum"})

# Output to CSV
summary.to_csv("output/summary.csv")
print("ETL complete. Summary saved.")

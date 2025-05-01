import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV data
df_csv = pd.read_csv('/mnt/data/sales_data_cleaned.csv')
print("CSV Data Loaded:")
print(df_csv.head())

# Step 2: Create SQLite DB and write table
conn = sqlite3.connect('sales_data.db')
df_csv.to_sql('sales', conn, if_exists='replace', index=False)
print("\nData inserted into SQLite database.")

# Step 3: Run SQL query for summary
query = """
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df_summary = pd.read_sql_query(query, conn)

# Step 4: Display results
print("\nSales Summary:")
print(df_summary)

# Step 5: Plot bar chart
plt.figure(figsize=(8, 5))
df_summary.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Optional: save chart
plt.show()

# Close connection
conn.close()

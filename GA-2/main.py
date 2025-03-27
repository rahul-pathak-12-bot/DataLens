import pandas as pd
from google.colab import files
uploaded = files.upload()

file_name = list(uploaded.keys())[0]
xls = pd.ExcelFile(file_name)


# Load sheets
sku_master_df = xls.parse("SKU MASTER")
sales_df = xls.parse("Sales")
opening_stock_df = xls.parse("Opening Stock")
stock_transfer_df = xls.parse("STOCK TRANSFER")

# Convert 'Date' column to datetime format
sales_df["Date"] = pd.to_datetime(sales_df["Date"])

# Merge sales with SKU master
sales_merged = sales_df.merge(sku_master_df, on="SKU")

# Compute Sale Value
sales_merged["Sale Value"] = sales_merged["Sales"] * sales_merged["Price"]

# 1. Total sale value of "LTA Wise City"
total_sale_value_lta = sales_merged[sales_merged["Product Name"] == "LTA Wise City"]["Sale Value"].sum()

# 2. Fraction of total sale quantity by "Books" category in first week
total_sales_first_week = sales_merged[(sales_merged["Date"] >= "2025-01-01") & (sales_merged["Date"] <= "2025-01-07")]["Sales"].sum()
books_sales_first_week = sales_merged[(sales_merged["Date"] >= "2025-01-01") & (sales_merged["Date"] <= "2025-01-07") & (sales_merged["Category"] == "Books")]["Sales"].sum()
books_sales_fraction = books_sales_first_week / total_sales_first_week if total_sales_first_week else 0

# 3. Maximum sale value by a single SKU in a day
max_sale_value_sku = sales_merged.groupby(["Date", "SKU"])["Sale Value"].sum().max()

# 4. Maximum revenue-generating category
max_revenue_category = sales_merged.groupby("Category")["Sale Value"].sum().idxmax()

# 5. Fraction of total sale value achieved by Mumbai
total_sale_value = sales_merged["Sale Value"].sum()
mumbai_sale_value = sales_merged[sales_merged["City"] == "Mumbai"]["Sale Value"].sum()
mumbai_sale_fraction = mumbai_sale_value / total_sale_value if total_sale_value else 0

# 6. Average days of inventory for SKU M003 in Pune
pune_stock_df = opening_stock_df[["SKU", "Pune"]].rename(columns={"Pune": "Opening Stock Pune"})
m003_sales_pune = sales_df[(sales_df["SKU"] == "M003") & (sales_df["City"] == "Pune")]["Sales"].sum()
opening_stock_m003_pune = pune_stock_df[pune_stock_df["SKU"] == "M003"]["Opening Stock Pune"].sum()
avg_days_inventory_m003_pune = opening_stock_m003_pune / (m003_sales_pune / 31) if m003_sales_pune else float('inf')

# 7. SKU with highest average days of inventory in Aurangabad
aurangabad_stock_df = opening_stock_df[["SKU", "Aurangabad"]].rename(columns={"Aurangabad": "Opening Stock Aurangabad"})
aurangabad_sales = sales_df[sales_df["City"] == "Aurangabad"].groupby("SKU")["Sales"].sum().reset_index()
aurangabad_inventory = aurangabad_stock_df.merge(aurangabad_sales, on="SKU", how="left").fillna(0)
aurangabad_inventory["Avg Days Inventory"] = aurangabad_inventory["Opening Stock Aurangabad"] / (aurangabad_inventory["Sales"] / 31)
highest_avg_inventory_sku_aurangabad = aurangabad_inventory.loc[aurangabad_inventory["Avg Days Inventory"].idxmax(), "SKU"]

# 8. Number of SKUs with at least one week's worth of inventory in Pune
pune_inventory = pune_stock_df.merge(sales_df[sales_df["City"] == "Pune"].groupby("SKU")["Sales"].sum().reset_index(), on="SKU", how="left").fillna(0)
pune_inventory["Avg Days Inventory"] = pune_inventory["Opening Stock Pune"] / (pune_inventory["Sales"] / 31)
skus_with_week_inventory_pune = (pune_inventory["Avg Days Inventory"] >= 7).sum()


# Print results
print("1. Total sale value of 'LTA Wise City':", total_sale_value_lta)
print("2. Fraction of total sales by 'Books' in first week:", books_sales_fraction)
print("3. Maximum sale value by a single SKU in a day:", max_sale_value_sku)
print("4. Maximum revenue-generating category:", max_revenue_category)
print("5. Fraction of total sale value achieved by Mumbai:", mumbai_sale_fraction)
print("6. Average days of inventory for SKU M003 in Pune:", avg_days_inventory_m003_pune)
print("7. SKU with highest average days of inventory in Aurangabad:", highest_avg_inventory_sku_aurangabad)
print("8. SKUs with at least one week's inventory in Pune:", skus_with_week_inventory_pune)

# 1. Total sale value of 'LTA Wise City': 13385200
# 2. Fraction of total sales by 'Books' in first week: 0.09187456796330044
# 3. Maximum sale value by a single SKU in a day: 5310000
# 4. Maximum revenue-generating category: Mobiles
# 5. Fraction of total sale value achieved by Mumbai: 0.3436950159452701
# 6. Average days of inventory for SKU M003 in Pune: 6.526315789473684
# 7. SKU with highest average days of inventory in Aurangabad: F003
# 8. SKUs with at least one week's inventory in Pune: 10
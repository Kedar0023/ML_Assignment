import pandas as pd
import random

# Generate sample data
product_ids = range(101, 151)  # 50 product IDs
product_names = [f"Product {i}" for i in product_ids]  # Generic product names
actual_sales = [random.randint(50, 300) for _ in product_ids]  # Random actual sales between 50 and 300
predicted_sales = [actual + random.randint(-20, 20) for actual in actual_sales]  # Predicted sales with some variance

# Create a dictionary for the data
data = {
    "Product ID": product_ids,
    "Product Name": product_names,
    "Actual Sales": actual_sales,
    "Predicted Sales": predicted_sales
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("cosmetic_shop_sales_50.csv", index=False)
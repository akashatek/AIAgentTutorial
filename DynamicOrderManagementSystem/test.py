from typing import Dict, TypedDict
import pandas as pd

# Load datasets
inventory_df = pd.read_csv("inventory.csv")
customers_df = pd.read_csv("customers.csv")

# Convert datasets to dictionaries
inventory = inventory_df.set_index("item_id").T.to_dict()
customers = customers_df.set_index("customer_id").T.to_dict()

print(inventory)
# # product_api.py

# def get_product_description(title):
#     # Simulate fetch from Walmart API using the title
#     mock_data = {
#         "bamboo toothbrush": "Made with biodegradable bamboo handle. Comes in recyclable box. Reusable and eco-friendly.It has recyclable content is high.",
#         "plastic toothbrush": "Made with synthetic plastic. Disposable and individually wrapped in plastic."
#     }
#     return mock_data.get(title.lower(), "No description found.")

import pandas as pd

# Load the dataset once at the start
try:
    df = pd.read_csv("datasets/products.csv")
except Exception as e:
    print("Error loading products.csv:", e)
    df = pd.DataFrame()  # fallback if loading fails

def find_product_by_title(title):
    """
    Finds the product by title using partial case-insensitive match.
    Returns the first matching product as a dictionary, or None.
    """
    if df.empty:
        return None

    match = df[df["title"].str.contains(title, case=False, na=False)]

    if not match.empty:
        return match.iloc[0].to_dict()
    
    return None



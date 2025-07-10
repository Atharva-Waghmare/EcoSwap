import pandas as pd
from scoring import score_from_response

# Load the dataset
df = pd.read_csv("datasets/products.csv")

# Function to score each row
def calculate_score(row):
    data = {
        "material": row["material"],
        "recycled_content": row["recycled_content"],
        "packaging": row["packaging"],
        "lifecycle": row["lifecycle"],
        "recyclability": row["recyclability"]
    }
    return score_from_response(data)

# Apply scoring
df["sustainability_score"] = df.apply(calculate_score, axis=1)

# Save the updated file
df.to_csv("datasets/products_scored.csv", index=False)
print("✅ Sustainability scores saved to products_scored.csv")

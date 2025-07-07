import pandas as pd
from sustainability_llm import analyze_sustainability_with_llm
from scoring import score_from_response

# Load the product dataset
df = pd.read_csv("products.csv")

# Store scores
scores = []

for i, row in df.iterrows():
    title = row.get("title", "")
    description = row.get("description", "")

    print(f"🔍 Processing: {title} ({i+1}/{len(df)})")

    llm_response = analyze_sustainability_with_llm(title, description)
    score = score_from_response(llm_response)

    scores.append(score)

# Add new column to DataFrame
df["sustainability_score"] = scores

# Save to new file
df.to_csv("products_scored.csv", index=False)

print("Done! File saved as 'products_scored.csv'")

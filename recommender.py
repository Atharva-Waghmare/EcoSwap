import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack, csr_matrix

def load_and_prepare_data(csv_file="datasets/products_scored.csv"):
    df = pd.read_csv(csv_file)
    df = df.dropna()

    # One-hot encode categorical columns
    categorical_cols = ["material", "recycled_content", "packaging", "lifecycle", "recyclability"]
    df_encoded = pd.get_dummies(df[categorical_cols])

    # Vectorize the title
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df["title"])

    # Combine features and convert to indexable format
    combined_features = hstack([tfidf_matrix, df_encoded])
    combined_features = csr_matrix(combined_features)  # ✅ Fix: convert to indexable

    return df, combined_features

def recommend_alternatives(product_name, df, features, top_n=3):
    if product_name not in df["title"].values:
        print("Product not found in dataset.")
        return

    idx = df[df["title"] == product_name].index[0]
    input_score = df.loc[idx, "sustainability_score"]

    # Compute cosine similarity
    sim_scores = cosine_similarity(features[idx], features).flatten()

    # Sort indices by similarity (excluding self)
    similar_indices = sim_scores.argsort()[::-1]

    recommended = 0
    print(f"\n Searching for better alternatives to '{product_name}' (score: {input_score})...\n")

    for i in similar_indices:
        if i != idx and df.loc[i, "sustainability_score"] > input_score:
            print(f"Alternative #{recommended + 1}:")
            print(f"Title: {df.loc[i, 'title']}")
            print(f"Score: {df.loc[i, 'sustainability_score']}")
            print(f"Material: {df.loc[i, 'material']}")
            print(f"Packaging: {df.loc[i, 'packaging']}")
            print("-" * 40)
            recommended += 1
            if recommended == top_n:
                break

    if recommended == 0:
        print("No more sustainable alternatives found.")

if __name__ == "__main__":
    df, features = load_and_prepare_data()

    # 🔍 Input product name from user
    input_product = input("Enter product title to find better alternatives: ").strip()
    recommend_alternatives(input_product, df, features, top_n=3)

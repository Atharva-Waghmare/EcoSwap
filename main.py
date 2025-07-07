from product_api import find_product_by_title
from scoring import score_from_response
from sustainability_llm import analyze_sustainability_with_llm

def main():
    title = input("🔍 Enter a product title: ").strip()
    product = find_product_by_title(title)

    if not product:
        print(" Product not found.")
        return

    print(f"\n Found Product: {product['title']}")
    print(f" Description: {product['description']}\n")

    llm_output = analyze_sustainability_with_llm(
        product['title'], product['description']
    )

    if not llm_output:
        print("Could not analyze sustainability.")
        return

    print("LLM Output (Parsed JSON):")
    for k, v in llm_output.items():
        print(f"  {k.capitalize()}: {v}")

    score = score_from_response(llm_output)
    print(f"\n Sustainability Score: {score}/100")

if __name__ == "__main__":
    main()

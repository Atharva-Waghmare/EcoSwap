import ollama
import json
import re

def extract_json(text):
    """
    Extract the first valid JSON object from the LLM response text.
    """
    match = re.search(r"\{.*?\}", text, re.DOTALL)
    return match.group(0) if match else "{}"

def analyze_sustainability_with_llm(title, description):
    """
    Uses an LLM via Ollama to extract sustainability attributes from a product's description.
    Returns a structured dictionary with keys: material, recycled_content, packaging, lifecycle, recyclability.
    """
    prompt = f"""
You are a sustainability analyst AI. Based on the following product title and description, extract key sustainability attributes.

Respond ONLY with a valid JSON object in this format:
{{
  "material": "fully_biodegradable / compostable / partially_biodegradable / recyclable_only / non_biodegradable",
  "recycled_content": "none / low / medium / high",
  "packaging": "plastic / recyclable / compostable / minimal / not mentioned",
  "lifecycle": "disposable / short-term / durable / reusable / long-lasting",
  "recyclability": "no / partially / yes"
}}

Title: {title}
Description: {description}
"""

    try:
        response = ollama.chat(
            model="mistral",  # or your preferred model like "mistral", "gemma"
            messages=[{"role": "user", "content": prompt}]
        )
        raw_output = response["message"]["content"]
        json_str = extract_json(raw_output)
        return json.loads(json_str)
    except Exception as e:
        print(f"LLM parsing failed: {e}")
        return {}

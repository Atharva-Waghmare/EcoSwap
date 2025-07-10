def normalize_value(value, mapping):
    for key, score in mapping.items():
        if key.lower() in value.lower():
            return score
    return 0

def score_from_response(response):
    material_score = normalize_value(response.get("material", ""), {
        "fully_biodegradable": 30,
        "compostable": 25,
        "partially_biodegradable": 20,
        "recyclable_only": 10,
        "non_biodegradable": 5
    })

    recycled_score = normalize_value(response.get("recycled_content", ""), {
        "none": 0,
        "low": 5,
        "medium": 10,
        "high": 15
    })

    packaging_score = normalize_value(response.get("packaging", ""), {
        "not mentioned": 0,
        "plastic": 5,
        "minimal": 10,
        "recyclable": 15,
        "compostable": 20
    })

    lifecycle_score = normalize_value(response.get("lifecycle", ""), {
        "disposable": 0,
        "short-term": 5,
        "durable": 10,
        "reusable": 15,
        "long-lasting": 20
    })

    recyclability_score = normalize_value(response.get("recyclability", ""), {
        "no": 0,
        "partially": 5,
        "yes": 10
    })

    total = material_score + recycled_score + packaging_score + lifecycle_score + recyclability_score
    return total

discounted = {
    pid: {
        "price": (
            val["price"] * 0.85 if val["category"] == "Electronics" and val["price"] > 50
            else val["price"] * 0.90 if val["category"] == "Fashion" and val["price"] > 50
            else val["price"]
        ),
        "category": val["category"]
    }
    for pid, val in products.items()
}
print(discounted)
products = {
    101: {"price": 120, "category": "Electronics"},
    102: {"price": 80, "category": "Fashion"},
    103: {"price": 40, "category": "Groceries"},                                                                                
    104: {"price": 60, "category": "Electronics"},
    105: {"price": 30, "category": "Fashion"},
}
VIOLATION_PRICES = {
    "broken_light": 50,
    "expired_tag": 75,
    "speeding": 120,
    "red_light": 150
}

def calculate_total(violations):
    total = 0
    items = []

    for violation in violations:
        price = VIOLATION_PRICES.get(violation, 0)
        items.append({
            "name": violation,
            "price": price
        })
        total += price

    return items, total
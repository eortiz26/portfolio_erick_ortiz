VIOLATION_PRICES = {
    "broken_light": 50,
    "expired_tag": 75,
    "speeding": 120,
    "red_light": 150
}

def make_line_items(violations):
    line_items = []
    total = 0

    for violation in violations:
        price = VIOLATION_PRICES.get(violation, 0)
        line_items.append({
            "violation": violation,
            "price": price
        })
        total = total + price

    return line_items, total
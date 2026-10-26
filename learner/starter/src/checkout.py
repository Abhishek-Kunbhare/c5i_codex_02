"""Small checkout example used in the Day 2 AGENTS.md lab."""


def calculate_total(items):
    """Return the total price for a sequence of {name, price, quantity} items.

    Prices are decimal values represented as Python floats for this teaching
    exercise. Production money code would normally use Decimal or integer minor
    units, but the visible contract for this lab intentionally uses float.
    """
    total = 0.0
    for item in items:
        total += float(item["price"]) * int(item["quantity"])
    return total

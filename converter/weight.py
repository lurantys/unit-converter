
def convert_weight(value, from_unit, to_unit):
    """Convert weight between kilograms, grams, and pounds."""

    factors = {
        "kg": 1,
        "g": 0.001,
        "lb": 0.45359237
    }

    if from_unit not in factors or to_unit not in factors:
        raise ValueError("Invalid weight unit")

    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("Weight must be a number")

    if value < 0:
        raise ValueError("Weight cannot be negative")

    weight_in_kg = value * factors[from_unit]
    result = weight_in_kg / factors[to_unit]

    return result

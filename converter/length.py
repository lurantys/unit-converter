"""Length conversions between meters, kilometers, centimeters and miles."""

# How many meters are in one of each unit
METERS_PER_UNIT = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mi": 1609.344,
}


def convert_length(value, from_unit, to_unit):
    """Convert a length from one unit to another.

    Supported units: "m", "km", "cm", "mi".
    Raises TypeError if value is not a number.
    Raises ValueError if value is negative or a unit is unknown.
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("value must be a number")
    if value < 0:
        raise ValueError("length cannot be negative")

    from_unit = str(from_unit).lower()
    to_unit = str(to_unit).lower()
    if from_unit not in METERS_PER_UNIT:
        raise ValueError(f"unknown unit: {from_unit}")
    if to_unit not in METERS_PER_UNIT:
        raise ValueError(f"unknown unit: {to_unit}")

    meters = value * METERS_PER_UNIT[from_unit]
    return meters / METERS_PER_UNIT[to_unit]

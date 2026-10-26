def convert_temperature(value, from_unit, to_unit):
    """Convert temperatures between Celsius, Fahrenheit, and Kelvin."""

    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Temperature must be a number")

    units = {"C", "F", "K"}

    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported temperature unit")

    # Convert to Celsius first
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if celsius < -273.15 - 1e-9:
        raise ValueError("Temperature cannot be below absolute zero")

    # Convert Celsius to the requested unit
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius * 9 / 5 + 32
    else:
        return celsius + 273.15
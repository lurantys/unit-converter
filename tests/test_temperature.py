import pytest
from converter.temperature import convert_temperature


def test_celsius_to_fahrenheit():
    assert convert_temperature(100, "C", "F") == 212


def test_fahrenheit_to_celsius():
    assert convert_temperature(32, "F", "C") == 0


def test_absolute_zero():
    assert convert_temperature(0, "K", "C") == pytest.approx(-273.15)


def test_below_absolute_zero():
    with pytest.raises(ValueError):
        convert_temperature(-1, "K", "C")


def test_invalid_unit():
    with pytest.raises(ValueError):
        convert_temperature(25, "C", "X")
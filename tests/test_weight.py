
import pytest
from converter.weight import convert_weight


def test_kg_to_grams():
    assert convert_weight(2, "kg", "g") == 3000


def test_grams_to_kg():
    assert convert_weight(500, "g", "kg") == 0.5


def test_kg_to_pounds():
    assert convert_weight(1, "kg", "lb") == pytest.approx(2.20462262)



def test_pounds_to_grams():
    assert convert_weight(1, "lb", "g") == pytest.approx(453.59237)


def test_zero_weight():
    assert convert_weight(0, "kg", "g") == 0


def test_negative_weight():
    with pytest.raises(ValueError):
        convert_weight(-5, "kg", "g")


def test_invalid_unit():
    with pytest.raises(ValueError):
        convert_weight(5, "kg", "meters")

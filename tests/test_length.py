import pytest

from converter.length import convert_length


def test_kilometers_to_meters():
    # normal case
    assert convert_length(2, "km", "m") == pytest.approx(2000)


def test_miles_to_kilometers():
    # normal case
    assert convert_length(1, "mi", "km") == pytest.approx(1.609344)


def test_zero_length_stays_zero():
    # edge / boundary case
    assert convert_length(0, "cm", "mi") == 0


def test_negative_length_raises_error():
    # invalid input
    with pytest.raises(ValueError):
        convert_length(-5, "m", "cm")


def test_unknown_unit_raises_error():
    # invalid input
    with pytest.raises(ValueError):
        convert_length(10, "m", "yard")
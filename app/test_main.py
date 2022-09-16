import pytest

from app.main import check_password


def test_should_return_false_for_long_password():
    assert check_password("Passwordanspassword3_") is False


def test_should_return_false_for_short_password():
    assert check_password("P3_s") is False


def test_should_return_false_without_upper():
    assert check_password("mateacademy3_") is False


def test_should_return_false_without_digit():
    assert check_password("MateAcademy_") is False


def test_should_return_false_without_special():
    assert check_password("MateAcademy3") is False


def test_should_return_true_for_valid_password():
    assert check_password("MateAcademy3_") is True


def test_raise_type_error():
    with pytest.raises(TypeError):
        check_password(235)

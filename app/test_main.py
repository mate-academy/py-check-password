import pytest

from app.main import check_password


def test_should_return_false_when_len_less_8() -> None:
    assert check_password("Key8@4!") is False


def test_should_return_false_when_len_more_than_16() -> None:
    assert check_password("Key8@4!Key8@4!Key8@4!") is False


def test_should_return_false_when_digit_less_1() -> None:
    assert check_password("K#&ey@Key!") is False


def test_should_return_false_when_upper_less_1() -> None:
    assert check_password("1#&ey@2ey!") is False


def test_should_return_false_when_special_less_1() -> None:
    assert check_password("1KeysL2eyp") is False


def test_should_return_false_when_letter_is_not_latin_alphabet() -> None:
    assert check_password("1KщysL2eyp") is False


def test_should_return_false_when_special_character_is_not_correct() -> None:
    assert check_password("1K+ysL2eyp") is False


def test_should_raise_error_if_data_is_int() -> None:
    with pytest.raises(TypeError):
        check_password(45)

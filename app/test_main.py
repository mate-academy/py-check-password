import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password",
    [
        pytest.param("Pass@word1", id="valid_password"),
        pytest.param("Pass@wo1", id="exactly_8_characters"),
        pytest.param("Pass@word1234567", id="exactly_16_characters"),
        pytest.param("Pa$@#&!-_1", id="all_allowed_special_characters"),
    ],
)
def test_should_return_true_for_valid_password(password: str) -> None:
    assert check_password(password) is True


@pytest.mark.parametrize(
    "password",
    [
        pytest.param("qwerty", id="too_short_without_requirements"),
        pytest.param("Str@ng", id="too_short"),
        pytest.param("Pass@w1", id="7_characters"),
        pytest.param("Pass@word12345678", id="17_characters"),
        pytest.param("pass@word1", id="without_uppercase_letter"),
        pytest.param("Pass@word", id="without_digit"),
        pytest.param("Password1", id="without_special_character"),
        pytest.param("Pass word@1", id="contains_space"),
        pytest.param("Pass%word1", id="contains_not_allowed_special"),
        pytest.param("Пароль@word1", id="contains_non_latin_letters"),
        pytest.param("", id="empty_password"),
    ],
)
def test_should_return_false_for_invalid_password(password: str) -> None:
    assert check_password(password) is False

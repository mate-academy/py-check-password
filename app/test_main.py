import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Pass*word1", False),
        ("Пасс@ворд1", False),
        ("Pass@word", False)
    ]
)
def test_if_check_password_accepts_only_valid_elements(
        password: str, result: bool) -> None:
    assert check_password(password) == result


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pas@1", False),
        ("!Password1", True),
        ("P2s@word", True),
        ("qwerty", False),
        ("Str@ng", False)
    ]
)
def test_if_check_password_has_at_least_8_elements(
        password: str, result: bool) -> None:
    assert check_password(password) == result


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word178jt!7", True),
        ("Password1#-78hj6frhj", False),
        ("Pass@word16798@g", True)
    ]
)
def test_if_check_password_has_maximum_16_elements(
        password: str, result: bool) -> None:
    assert check_password(password) == result


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Password!", False),
        ("Pass568word", False),
        ("pass@word1", False)
    ]
)
def test_if_check_password_contains_at_least_1_not_word(
        password: str, result: bool) -> None:
    assert check_password(password) == result

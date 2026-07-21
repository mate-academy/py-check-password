import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pass@word134547", True)
    ]
)
def test_valid_password(password: str, result: bool) -> None:
    assert check_password(password) == result


def test_should_check_max_length() -> None:
    assert not check_password("Pass@word134547hyy"), \
        "Password max length should be 17 symbols"


def test_should_check_min_length() -> None:
    assert not check_password("P@wrd13"), \
        "Password min length should be 8 symbols"


def test_should_check_digit() -> None:
    assert not check_password("P@wrdurttd"), \
        "Password should contain digits"


def test_should_check_upper_letter() -> None:
    assert not check_password("p@wrdurttd1112"), \
        "Password should contain upper letter"


def test_should_check_special_symbols() -> None:
    assert not check_password("Pawrdurttd1112"), \
        "Password should contain special symbols"

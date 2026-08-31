import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param("", False, id="Passed empty string"),
        pytest.param("W3q#f", False, id="Passed too short string"),
        pytest.param("qwertyuiopasdfghjklA!44", False,
                     id="Passed too long string")
    ]
)
def test_fails_if_wrong_len(value: str, expected: bool) -> None:
    assert (check_password(value) == expected), \
        "Password must have length of 8-17 symbols"


def test_fails_if_contains_unsuitable_symbol() -> None:
    assert (check_password("%dfghjklA!4") is False)
    assert (check_password("dfghjklA!4+") is False)


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param("dfghjklA!", False, id="No digit"),
        pytest.param("dfghjklA4", False, id="No special symbol"),
        pytest.param("wqewgdfg!3", False, id="No upper case")
    ]
)
def test_test_fails_if_no_upperletter_digit_specsymbol(
        value: str, expected: bool
) -> None:
    assert (check_password(value) == expected)


def test_returns_bool() -> None:
    assert (isinstance(check_password("dfghjklA!4+"), bool) is True)
    assert (isinstance(check_password("dfghjk!4+"), bool) is True)
    assert (isinstance(check_password(""), bool) is True)

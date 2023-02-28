import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Abcdefg1$", True, id="Test for a valid password"
        ),
        pytest.param(
            "Abc123!",
            False,
            id="Test for a password that is too short",
        ),
        pytest.param(
            "Abcdefghij$",
            False,
            id="Test for a password that is too long",
        ),
        pytest.param(
            "Abcdefghij1",
            False,
            id="Test for a password that does not contain a special character",
        ),
        pytest.param(
            "abcdefg1$",
            False,
            id="Test for a password that does not contain an uppercase letter",
        ),
        pytest.param(
            "aBc1$",
            False,
            id="Test for a password that contains only"
               " allowed characters but is too short",
        ),
        pytest.param(
            "aBcdeFgHiJk1aaa$#M",
            False,
            id="Test for a password that contains only "
               "allowed characters but is too long",
        ),
        pytest.param("", False, id="Test for an empty password:"),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

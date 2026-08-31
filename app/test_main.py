import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "passwrd, return_bool",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="Valid password"
        ),
        pytest.param(
            "1qwerty@",
            False,
            id="No 'upper' case letters"
        ),
        pytest.param(
            "Qwe1ty@",
            False,
            id="Password is too short"
        ),
        pytest.param(
            "Pass@word1Pass@word1Pass@word1",
            False,
            id="Password is too long"
        ),
        pytest.param(
            "Pass@word",
            False,
            id="Password has no digits"
        ),
        pytest.param(
            "Pass1word",
            False,
            id="Password has no symbols"
        ),
    ]
)
def test_check_password(passwrd: str, return_bool: bool) -> None:
    assert check_password(passwrd) == return_bool

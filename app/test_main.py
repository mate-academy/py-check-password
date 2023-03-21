import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Pass@word1", True,
                     id="Password is correct"),
        pytest.param("оарраівраллар", False,
                     id="Password alphabet Aa-Zz"),
        pytest.param("Str@ng", False,
                     id="Password have at least 8 characters"),
        pytest.param("Pass@word1Pass@word1Pass@word1",
                     False, id="Password have maximum"
                               " 16 characters inclusive"),
        pytest.param("Pass@1",
                     False, id="Password have 8"),
        pytest.param("Password", False,
                     id="Password contains at least 1 digit,"
                        " 1 special character, 1 uppercase letter"),
        pytest.param("Password1", False,
                     id="Password contains 1 special "
                        "character, 1 uppercase letter"),
        pytest.param("PasswGFJKd1", False,
                     id="Password contains 1 uppercase letter"),
        pytest.param("password1@", False,
                     id="Password contains 1 uppercase letter"),
        pytest.param("Password@", False,
                     id="Password contains 1 uppercase letter")
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result

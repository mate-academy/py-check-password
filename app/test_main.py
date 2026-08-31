import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Pass@word1", True,
                     id="valid password"),
        pytest.param("Pass1@r", False,
                     id="short password"),
        pytest.param("Str@ngShpomnmt1hyt", False,
                     id="password is too long"),
        pytest.param("П@роль123", False,
                     id="password contains invalid characters"),
        pytest.param("P@ssword", False,
                     id="password must contain at least one number"),
        pytest.param("p@ssword1", False,
                     id="password must contain at least one capital letter"),
        pytest.param("Password1", False,
                     id="password must contain at least one special character")
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

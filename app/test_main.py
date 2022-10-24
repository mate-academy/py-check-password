import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, data", [
        pytest.param("Pass@word1", True,
                     id="Test Pass@word1 should return True"),
        pytest.param("qwerty1@", False,
                     id="Test without uppercase letter"),
        pytest.param("Qwert@sdf", False,
                     id=" Tests without digits"),
        pytest.param("Qwerty123", False,
                     id="Test without special character"),
        pytest.param("Qwerty123@321ytrewq", False,
                     id="Test too long password"),
        pytest.param("Q@we1", False,
                     id="Test too short password")
    ]
)
def test_password_checker(password: str, data: bool) -> None:
    assert check_password(password) == data

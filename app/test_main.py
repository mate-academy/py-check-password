import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected", [
        pytest.param("Pass@word1", True,
                     id="Valid password"),
        pytest.param("qwertyQWERTY", False,
                     id="Should return False while only letters"),
        pytest.param("Passw@rd", False,
                     id="Should return False without digit"),
        pytest.param("Password123", False,
                     id="Should return False without special char"),
        pytest.param("123123123", False,
                     id="Should return False when only digits"),
        pytest.param("Pass1@", False,
                     id="Should return false when len < 8"),
        pytest.param("Pass@word1Pass@word1", False,
                     id="Should return False when len > 16 "),
        pytest.param("pass@word1", False,
                     id="Should return False without upper letter")
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("M@nLen8", False),
        ("Qwerty123", False),
        ("qwerty123$", False),
        ("Qwerty$$", False),
        ("Qwerty12345", False),
        ("Qwerty1234", False),
        ("Qwerty17M@xLength", False),
    ]
)
def test_check_password(password: str, expected: str) -> None:
    assert check_password(password) == expected

import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("Pas$w0rd", True),
        ("Pass@word1Pass@1", True),
        ("Short@1", False),
        ("Passw0rdPassw0rdPa$sw0rd", False),
        ("Password!", False),
        ("Passw0rd", False),
        ("passw0rd!", False),
        ("Passw0rd!%", False),
        ("", False)
    ],
    ids=[
        "Valid Password", "Valid min length", "Valid max length",
        "Invalid too short", "Invalid too long", "Invalid no digit",
        "Invalid no special", "No upper letter", "Invalid symbol %",
        "Invalid empty str"
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

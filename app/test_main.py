import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_valid",
    [
        ("", False),
        ("Pass@word1", True),
        ("Qwerty132", False),
        ("No!digits", False),
        ("Looooooooooong-password228", False),
        ("1Shrt_p", False),
        ("Great&passwоrd100", False),
        ("no-upper00", False)
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid

from pytest import mark
from app.main import check_password


@mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("Password", False),
        ("qwerty1", False),
        ("Str@ng", False),
        ("P@ssw0rd", True),
        ("Short1!", False),
        ("ThisPasswordIsWayTooLong1@", False),
        ("Valllid1@", True),
        ("noDigits@", False),   # No digits
        ("NoSpecial1", False),  # No special character
        ("noupper1@", False),   # No uppercase letter
    ],
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

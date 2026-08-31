import pytest

from app.main import check_password


@pytest.mark.parametrize(
    ("password", "expected"),
    [
        ("Pass@word1", True),
        ("Pass@word1Pass@word1", False),
        ("Pa@1", False),
        ("123456789", False),
        ("qwerty123", False),
        ("qweRty123", False),
        ("qwerty@12", False),
        ("qwerty@Ty", False)
    ],
    ids=[
        "Function should return 'True' when password Pass@word1",
        "Maximum password length should be 16 characters",
        "Minimum password length should be 8 characters",
        "Function should return 'False' when password contain only numbers",
        "Password also should contain 1 special character, 1 uppercase",
        "Password also should contain at least 1 special character",
        "Password also should contain at least 1 uppercase",
        "Password also should contain at least 1 digit"
    ]
)
def test_check_password(password: str,
                        expected: bool) -> None:

    assert check_password(password) == expected

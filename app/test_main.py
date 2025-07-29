import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_validation",
    [
        ("12345678", False),
        ("$$$$$$$$", False),
        ("Password", False),
        ("Password_", False),
        ("Test123@", True),
        ("Test 123@", False),
        ("Test123@%", False),
        ("Test12@", False),
        ("Test12#Test12#12", True),
        ("Test12@Test12@123", False),
        ("Test1$@#&!-_", True),
        ("Test$@#&!-_", False),
        ("test$@#&!1-_", False),
        ("Test1234", False),
    ],
)
def test_password_should_be_validated(
    password: str, expected_validation: bool
) -> None:
    assert check_password(password) == expected_validation

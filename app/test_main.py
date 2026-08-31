import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    # Valid passwords
    ("Pass@word1", True),
    ("Str0ng-P@ss", True),
    ("P@ssword1234", True),
    ("Abc$1234", True),  # minimum length with all criteria met
    ("MaxLength$1234Ok", True),  # maximum length with all criteria met

    # Invalid due to length
    ("Short1@", False),  # less than 8 characters
    ("ThisIsAVeryL0ngPassword!", False),  # more than 16 characters

    # Missing character type
    ("password1234", False),  # no uppercase letter or special character
    ("PasswordOnly", False),  # no digit or special character
    ("Passw0rd", False),  # no special character
    ("NoSpecial123", False),  # no special character
    ("NOLOWERCASE123$", False),  # no lowercase letter

    # Invalid characters
    ("Pass@word1%", False),  # contains an invalid character "%"
    ("Pass@word1*", False),  # contains an invalid character "*"
    ("Invalid#Char{", False)  # contains an invalid character "{"
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected, f"Failed on {password}"

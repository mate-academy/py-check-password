import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected", [
        ("Pass@word1", True),
        ("Abc@1234", True),
        ("Valid123!", True),
        ("Test@Pass1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Password@!", False),
        ("NoSpecial123", False),
        ("password123!", False),
        ("A1!sh", False),
        ("A1!thisIsALongPassword123!", False),
        ("Invalid!#*", False),
    ]
)
def test_check_password(password: str, expected: str) -> None:
    assert check_password(password) == expected

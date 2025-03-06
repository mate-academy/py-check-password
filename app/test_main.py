import pytest

from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("", False),
    ("Abc12@", False),
    ("AaBbCcDd11223344@$#!", False),
    ("AaBbCc123", False),
    ("AaBbCc@###@", False),
    ("1234@###@", False),
    ("aabbcc123!", False),
    ("Aabb cc123!", False),
    ("Aabb*cc123!", False),
    ("Aabbcc123!", True),
    ("A1@abcde", True),
    ("A1@abcdefghi1234", True)
], ids=[
    "empty password",
    "too short password",
    "too long password",
    "missing special character",
    "missing digit",
    "missing letter",
    "missing uppercase letter",
    "password contains space",
    "password contains forbidden character",
    "valid password",
    "valid password with min length",
    "valid password with max length"
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

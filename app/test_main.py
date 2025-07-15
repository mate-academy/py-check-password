import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("pass@word1", False),
        ("Password1", False),
        ("Pass@word", False),
        ("Passsssssssssssssssssssssssssssword1", False),
        ("pwd", False),
        ("Pass@1", False),
        ("Pass@word1234567", True),
        ("Pass@word12345678", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

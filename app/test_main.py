import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("very_long_Pass@1", True),
        ("very11ong1Pass@word", False),
        ("Pass@12", False),
        ("Pass@123", True),
        ("Pass@withno", False),
        ("noupper@1", False)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

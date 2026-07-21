from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("Qwe@t1", False),
        ("Strng143124", False),
        ("123456789", False),
        ("dfkdfhaAAsdf", False),
        ("fdfsdfdf@3422", False),
        ("Fefwef123sd@fffjaldk3434534", False),
        ("SVdfsdfs@@", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

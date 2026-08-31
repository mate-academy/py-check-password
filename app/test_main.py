import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("aA1@BcCdD", True),
        ("1A@a1", False),
        ("adddCC12464615542@@@@@444$$$@#@#@@@@##", False),
        ("Aa$ffFjdj", False),
        ("Aavv4522333", False),
        ("ada4gcc@@$c", False),
    ],
    ids=[
        "Valid with correct password",
        "Non valid if characters < 8",
        "Non valid if characters more than 16",
        "Non valid if no digit",
        "Non valid if no special character",
        "Non valid if no uppercase"
    ]
)
def test_password_function(password: str,
                           expected: bool
                           ) -> None:
    assert check_password(password) == expected

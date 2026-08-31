import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "actual_password,checking_password",
    [
        ("Pass@word1", True),
        ("$tr!k3_Em", True),
        ("Day@n1ght&sl#-y", True),
        ("greedisgood", False),
        ("qwerty", False),
        ("Whosyourdaddy1seede@dpeople", False),
        ("$@#&!-_1", False),
        ("N@D1ddy", False),
        ("OnlyLettersAndDigits", False),
        ("12345678", False),
        ("ALLUPPERCASE1@", True),
        ("lowercaseandl1", False),
        ("validPASSWORD!", False),
        ("Pa$$word", False),
        ("P@ss w1th space", False),
        ("Pass5qwer", False),
    ]
)
def test_check_password(actual_password: str, checking_password: bool) -> None:
    assert check_password(actual_password) == checking_password

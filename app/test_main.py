import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1_аБв", False),
        ("P@wo1", False),
        ("Pss_wrd1", True),
        ("Pass@word1Pass!word1", False),
        ("Pass_wd1Ps@word1", True),
        ("Pass#word", False),
        ("Password1", False),
        ("pass@word1", False),
        ("passwordlower", False),
        ("PASSWORDUPPER", False),
        ("1234567890", False),
        ("$@#&!-_$@#&!-_", False),
        ("Pass@word1", True),
    ],
    ids=[
        "not acceptable letter",
        "length is less than allowed",
        "length is on the lower edge",
        "length is biger than allowed",
        "length is on the upper edge",
        "has no digit",
        "has no special character",
        "has no uppercase letter",
        "only lower letters",
        "only upper letters",
        "only digits",
        "only special characters",
        "valid password",
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) is result

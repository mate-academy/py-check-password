import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("Pass@word1", True),
        ("Pass`word1", False),
        ("12345A@", False),
        ("Pass@word12345678", False),
        ("123456a@", False),
        ("1234567A", False),
        ("@@@@AAAA", False),

    ],
    ids=[
        "only letters Aa-Zz, digits 0-9 or special character $@#&!-_",
        "should NOT accept special character out of $@#&!-_",
        "should contain at least 8 characters",
        "should contain maximum 16 characters inclusive",
        "should contain at least 1 uppercase letter",
        "should contain at least 1 special character",
        "should contain at least 1 digit",
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

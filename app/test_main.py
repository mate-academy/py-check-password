import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Fs", False),
        ("ff@sdf1", False),
        ("Пhln#1sdfg", False),
        ("F1sdfdfka", False),
        ("F1sdfdfka$asdsdsgfgdfdfdf", False),
        ("F@sfd,dfdfbg", False),
        ("1passwOrd@", True),
    ],
    ids=[
        "shorter than 6 symbols",
        "without uppercase letter",
        "with not Latin letters",
        "without special symbols",
        "More than 16 symbols",
        "Without digits",
        "Correct password"
    ]
)
def test_checking_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

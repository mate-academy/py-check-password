import pytest

from app.main import check_password


@pytest.mark.parametrize(
    ("password, expected"),
    [
        ("Pass@word1", True),
        ("P@1_fs", False),
        ("Str@ng", False),
        ("Pass@word1fsdffsf", False),
        ("passw1@ord", False),
        ("PF1lfsSDGSF", False),
        ("PF@_fsSDGSF", False),

    ],
    ids=[
        "Function should return True when all conditions complied with",
        "Password should contains at least 8 characters",
        ("Password should contains at least 1 digit,"
         " 1 special character, 1 uppercase letter."),
        "Password should contains 16 characters inclusive",
        "Password should contains al leas 1 uppercase",
        "Password should contains al leas 1 special symbol",
        "Password should contains al leas 1 digit",
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

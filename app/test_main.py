import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Good_password1", True),
        ("111111", False),
        ("normal_password", False),
        ("Iron_man89", True),
        ("super_pass11", False),
        ("Pass_1", False),
        ("Newpassword6", False),
        ("Enter_matrix", False),
        ("Very_good_super_password_in_the_world11111", False)
    ],
    ids=[
        "1 digit, 1 special symbol, 1 uppercase letter is good password",
        "Password should be longer than 8 symbols",
        "Password should be longer than 8 symbols",
        "1 digit, 1 special symbol, 1 uppercase letter is good password",
        "Password should contains at 1 special character, 1 uppercase letter",
        "Password should contains 1 digit and 1 uppercase letter",
        "1 digit, 1 special symbol, 1 uppercase letter is good password",
        "Password should contains 1 uppercase  letter",
        "Password too short",
        "Password should contains 1 special symbol",
        "Password should contains 1 digit symbol",
        "Password shold be not longer than 17 symbols"
    ]
)
def test_check_password(password: str, result: str) -> None:
    assert check_password(password) == result

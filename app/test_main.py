import pytest

from app.main import check_password


# def test_check_password():
#     password = 'Pass@word1'
#     assert check_password(password) == True
#
#
# def test_check_password_with_out_uppercase_letter():
#     password = 'pass@word1'
#     assert check_password(password) == False
#
#
# def test_check_password_with_out_digits():
#     password = 'Pass@word'
#     assert check_password(password) == False
#
#
# def test_check_password_with_out_special_symbol():
#     password = 'Password1'
#     assert check_password(password) == False
#
#
# def test_check_password_with_short_password():
#     password = 'Passw@1'
#     assert check_password(password) == False
#
#
# def test_check_password_with_long_password():
#     password = 'Passwwwwwwwwwwww@@@1'
#     assert check_password(password) == False


@pytest.mark.parametrize(
    "password  ,expect_result",
    [
        ("Pass@word1", True),
        ("pass@word1", False),
        ("Pass@word", False),
        ("Password1", False),
        ("Passw@1", False),
        (
            "Passwwwwwwwwwwww@@@1",
            False,
        ),
    ],
)
def test_check_passwords(password: str, expect_result: str) -> None:
    password = password
    assert check_password(password) == expect_result

from pytest import mark

from app.main import check_password


@mark.parametrize("password,expected", [
    ("Pass@word1", True),
    ("TooLongPassword....1", False),
    ("shoRt2_", False),
    ("no_digits_Passw", False),
    ("noSpecSymbols1", False),
    ("just_lowercase_1", False),
    ("not_lАТІН_1", False),
    ("1_moreNice-Passw", True)
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

from pytest import mark

from app.main import check_password


@mark.parametrize(
    "password,expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Пароль@1", False),
        ("Pass@word1*", False)
    ],
    ids=[
        "Should return True",
        "If contain only lower letters, should return False",
        "If not contain 1 digit, should return False",
        "If contain not only Latin letters, should return False",
        "If contain character not from $@#&!-_, should return False"
    ]
)
def test_check_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result

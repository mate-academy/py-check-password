from pytest import mark

from app.main import check_password


@mark.parametrize(
    "password,expected_value",
    [
        ("Pass@word1", True),
        ("a1-C", False),
        ("A-1asdfg", True),
        ("qwerty", False),
        ("sh@rt!2", False),
        ("abCd1#-ddajondersawdwasd", False),
        ("12345678910123456", False),
        ("pasSword", False),
        ("pAssword1", False),
        ("passw!rd2", False),
        ("pass-word", False),
        ("$password2", False),
        ("#passWord", False)
    ],
    ids=[
        "Correct password",
        "short pass",
        "correct pass len 8 symbols",
        "Short password less 8 symbols",
        "short password",
        "extra long password",
        "long password more then 16 symbols",
        "Big letter no spec symbol,no digit",
        "Big letter and digit no spec symbol",
        "No big letter spec symbol digit",
        "No big letter no digit",
        "Spec symbol digit not bog letter",
        "Spec symbol big letter no digit"
    ]
)
def test_check_password(password: str, expected_value: bool) -> None:
    assert check_password(password) == expected_value

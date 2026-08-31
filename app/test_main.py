import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, check_result",
    [
        ("Pass@word1", True),
        ("Short#2", False),
        ("NoSpecial12", False),
        ("no_uppercase#3", False),
        ("NO_digits@pass", False),
        ("Tooooo_Loo@oo0g!!", False),
        ("Wrong_char:@1", False),
        ("Не_Латинка_54", False),
        ("Again_OK@640", True),
    ],
    ids=[
        "Correct passwd",
        "to short passwd",
        "passwd has no specials",
        "passwd has no uppercase",
        "passwd has no digits",
        "passwd is to long",
        "passwd has frobidden char",
        "passwd has not Latin letter(s)",
        "Correct passwd",
    ]
)
def test_if_password_is_valid(password: str, check_result: bool) -> None:
    assert check_password(password) == check_result, \
        "password does not match the condition(s)"

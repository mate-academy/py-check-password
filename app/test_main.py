from app.main import check_password


def test_check_password() -> None:
    assert check_password("Pass@word1") is True
    assert check_password("qwerty") is False
    assert check_password("Str@ng") is False
    assert check_password("Aa1!aaaa") is True
    assert check_password("Short1!") is False
    assert check_password("NoNumbers!!") is False
    assert check_password("noSpecials123") is False
    assert check_password("ALLCAPS@1") is True
    assert check_password("lowercase@1") is False
    assert check_password("TooLongPassword@12345") is False
    assert check_password("Valid$Pass9") is True
    assert check_password("Another$Pass8") is True
    assert check_password("NoSpecialOrNumber") is False
    assert check_password("Valid_123Aa") is True
    assert check_password("Invalid Space 1!") is False
    assert check_password("!@#&-123A") is True
    assert check_password("abcdefgh") is False
    assert check_password("ABCDEFGH") is False
    assert check_password("12345678") is False
    assert check_password("abcdefgh1!") is False

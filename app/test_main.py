from app.main import check_password


def test_check_password() -> None:
    assert check_password("abcdefghifds@1") is False
    assert check_password("Pass@word1") is True
    assert check_password("qwerty") is False
    assert check_password("Str@ng") is False
    assert check_password("Abcdefg1@") is True
    assert check_password("Abcdefg1") is False
    assert check_password("Abcdefg@") is False
    assert check_password("Abcdefghijklmnop1$") is False
    assert check_password("Abcdefghijklmnop1") is False
    assert check_password("Abcdefghijklmn$") is False
    assert check_password("Abcdefghijklmno1") is False
    assert check_password("Abcdefghijklmno$") is False
    assert check_password("Abc$2") is False

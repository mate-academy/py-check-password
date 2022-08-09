from app.main import check_password


def test_password_too_short():
    assert not check_password("Q1@s")


def test_password_too_long():
    assert not check_password("Pass@word1Pass@word1Pass@word1Pass@word1")


def test_password_whitouht_upper_case():
    assert not check_password("pass@word1")


def test_password_whitouht_digit():
    assert not check_password("pass@wordd")  #


def test_password_whitouht_special_characters():
    assert not check_password("passwword1")

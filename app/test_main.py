from app.main import check_password


def test_check_password_where_all_right() -> None:
    assert check_password("Pass@word1")


def test_check_password_where_contain_not_latin_alphabet() -> None:
    assert not check_password("Pass@word1чф")


def test_check_password_where_contain_unauthorized_special_character() -> None:
    assert not check_password("Pass@word1?")


def test_check_password_where_len_less_8() -> None:
    assert not check_password("Ps@wod1")


def test_check_password_where_len_more_16() -> None:
    assert not check_password("Pass@word1Pass@word1")


def test_check_password_where_not_contain_digit() -> None:
    assert not check_password("Pass@word")


def test_check_password_where_not_contain_special_character() -> None:
    assert not check_password("Password1")


def test_check_password_where_not_contain_upper() -> None:
    assert not check_password("pass@word1")

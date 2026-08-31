from app.main import check_password


def test_normal_password() -> None:
    assert check_password("Pass@word1") is True


def test_less_8_symbols() -> None:
    assert check_password("Q1@rty") is False


def test_more_16_symbols() -> None:
    assert check_password("Qwe@rtyqwertyqw1erty") is False


def test_without_number() -> None:
    assert check_password("Qwer@tyqwer") is False


def test_without_big_letter() -> None:
    assert check_password("qwe@rwwert1") is False


def test_witout_special_symbol() -> None:
    assert check_password("Q1wertyqwe") is False

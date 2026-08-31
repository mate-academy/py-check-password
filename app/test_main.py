from app.main import check_password


def test_short_password() -> None:
    assert check_password("@2ertY") is False


def test_long_password() -> None:
    assert check_password("Q2erty_qwerty_qwerty_qwerty") is False


def test_without_digit() -> None:
    assert check_password("My_password") is False


def test_without_special_char() -> None:
    assert check_password("My0password") is False


def test_without_uppercase() -> None:
    assert check_password("my_1password") is False


def test_cyrillic_letter() -> None:
    assert check_password("My_Пassword") is False


def test_acceptable() -> None:
    assert check_password("My_p2ssword") is True

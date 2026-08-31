from app.main import check_password


def test_password_on_cyrillic_alphabet() -> None:
    password = "123Пароль$@#&"
    assert check_password(password) is False


def test_password_on_latin_alphabet() -> None:
    password = "123ADcd@#&"
    assert check_password(password) is True


def test_password_on_lowercase_alphabet() -> None:
    password = "asdasd123$@#&"
    assert check_password(password) is False


def test_password_contain_uppercase_letters() -> None:
    password = "Aa124@#123asd"
    assert check_password(password) is True


def test_password_without_special_characters() -> None:
    password = "1231AAdf"
    assert check_password(password) is False


def test_password_less_than_eight_characters() -> None:
    password = "1A#1adA"
    assert check_password(password) is False


def test_password_greater_than_sixteen_characters() -> None:
    password = "1A#1adAa1A#1adAa1A#1adAa1A#1adAa1A#1adAa"
    assert check_password(password) is False


def test_password_without_digits() -> None:
    password = "AAAaaa#####"
    assert check_password(password) is False

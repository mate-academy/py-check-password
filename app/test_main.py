from app.main import check_password


def test_check_password_logic() -> None:
    password = "Password@123"
    expected = True
    actual = check_password(password)
    assert expected == actual


def test_check_password_without_upper() -> None:
    password = "password@123"
    expected = False
    actual = check_password(password)
    assert expected == actual


def test_check_password_without_digit() -> None:
    password = "Password@"
    expected = False
    actual = check_password(password)
    assert expected == actual


def test_check_password_without_special_char() -> None:
    password = "Password123"
    expected = False
    actual = check_password(password)
    assert expected == actual


def test_check_password_not_in_ascii() -> None:
    password = "密码@123"
    expected = False
    actual = check_password(password)
    assert expected == actual


def test_check_password_is_shorter() -> None:
    password = "Pass@12"
    expected = False
    actual = check_password(password)
    assert expected == actual


def test_check_password_is_longer() -> None:
    password = "Password@123!$456"
    expected = False
    actual = check_password(password)
    assert expected == actual

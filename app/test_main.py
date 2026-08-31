from app.main import check_password


def test_should_check_min_length() -> None:
    password = "s"
    assert check_password(password) is False
    password = "jd&H12"
    assert check_password(password) is False
    password = ("Pasord@2")
    assert check_password(password) is True


def test_should_return_false_if_pass_is_to_long() -> None:
    password = "Password@123rwfwfwffwf"
    assert check_password(password) is False
    password = ("Password@123")
    assert check_password(password) is True


def test_should_return_false_if_pass_doesnt_have_digit() -> None:
    password = "Password@"
    assert check_password(password) is False
    password = ("Password@123")
    assert check_password(password) is True


def test_should_return_false_if_pass_doesnt_have_special_simbols() -> None:
    password = "Password123"
    assert check_password(password) is False
    password = ("Password@123")
    assert check_password(password) is True


def test_should_return_false_if_pass_doesnt_have_upper_letter() -> None:
    password = "assword@123"
    assert check_password(password) is False
    password = ("Password@123")
    assert check_password(password) is True

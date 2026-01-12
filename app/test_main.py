from app.main import check_password


def test_should_check_too_long_password() -> None:
    assert check_password("Anhchcjdkjxcjcj1@cjcnkdk") is False


def test_should_check_too_short_password() -> None:
    assert check_password("S2@nh") is False


def test_should_check_password_without_digits() -> None:
    assert check_password("Whchcjdk#jxc") is False


def test_should_check_password_without_uppercase_letter() -> None:
    assert check_password("hchc2jdk#jxc") is False


def test_should_check_correct_password() -> None:
    assert check_password("Pass@word1") is True

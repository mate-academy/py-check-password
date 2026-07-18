from app.main import check_password


def test_should_check_digit() -> None:
    assert check_password("Pass@word") is False


def test_should_check_special_symbols() -> None:
    assert check_password("Password1") is False


def test_should_check_min_length() -> None:
    assert check_password("P1@") is False


def test_should_check_upper_length() -> None:
    assert check_password("pass@word1") is False


def test_should_check_max_length() -> None:
    assert check_password("Pass2word1234qwertyHelloWorl@1") is False


def test_should_check_function_working_correctly() -> None:
    assert check_password("Pass@word1") is True

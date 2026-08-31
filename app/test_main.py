from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1")


def test_short_password() -> None:
    assert not check_password("qwerty")


def test_missing_special() -> None:
    assert not check_password("Password1")


def test_missing_upper() -> None:
    assert not check_password("pass@word1")


def test_missing_digit() -> None:
    assert not check_password("Pass@word")


def test_invalid_characters() -> None:
    assert not check_password("Päss@word1")


def test_max_length() -> None:
    assert check_password("Pass@word123456")


def test_exceed_max_length() -> None:
    assert not check_password("Pass@word123456789")

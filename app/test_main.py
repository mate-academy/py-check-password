from app.main import check_password


def test_check_password_valid() -> None:
    assert check_password("Pass@word1") is True


def test_check_password_lowercase() -> None:
    assert check_password("qwertyhhhhhhh") is False


def test_check_password_no_digits() -> None:
    assert check_password("Str@ngSSSSSS") is False


def test_check_password_uppercase() -> None:
    assert check_password("STDDDBDDDDDD") is False


def test_check_password_empty() -> None:
    assert check_password("") is False


def test_check_password_all_digits() -> None:
    assert check_password("1145555555") is False


def test_check_password_no_special_character() -> None:
    assert check_password("Str1nghhhggff") is False


def test_check_password_no_uppercase() -> None:
    assert check_password("t5r1n!gttt") is False


def test_check_password_too_short() -> None:
    assert check_password("S1@hh") is False


def test_check_password_too_long() -> None:
    assert check_password("S1@hhrrrrrrrrrrrrr") is False

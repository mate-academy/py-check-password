from app.main import check_password


def test_password_is_short() -> None:
    assert not check_password("A12345!")


def test_password_is_long() -> None:
    assert not check_password("ABCDEFGHIJK1234567!!!!!!!")


def test_password_no_special_char() -> None:
    assert not check_password("ABCDEFG123")


def test_password_correct() -> None:
    assert check_password("ABCDEF123!")


def test_no_digit() -> None:
    assert not check_password("ABCdefgHiJ!!!")


def test_no_upper_letters() -> None:
    assert not check_password("abcdefg1!!!!!!")

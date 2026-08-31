from app.main import check_password


def test_too_long() -> None:
    assert check_password("Str@ng1man19032409") is False


def test_too_short() -> None:
    assert check_password("Str@ng1") is False


def test_no_digit() -> None:
    assert check_password("Str@ngiee") is False


def test_no_upper() -> None:
    assert check_password("qwerty@24") is False


def test_no_special() -> None:
    assert check_password("Password1") is False


def test_valid_password() -> None:
    assert check_password("P@ssword1") is True

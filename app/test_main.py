from app.main import check_password


def test_correct_password() -> None:
    assert check_password("Arh6-3shah") is True


def test_password_without_digits() -> None:
    assert check_password("Mrjerks&") is False


def test_password_with_short_password() -> None:
    assert check_password("1-rB") is False


def test_too_long_password() -> None:
    assert check_password("zxcvbnAsfvf6vbfd2-") is False


def test_password_without_special_characters() -> None:
    assert check_password("Arb56jmd") is False


def test_password_without_upper_case() -> None:
    assert check_password("qwe123-f-ff4") is False

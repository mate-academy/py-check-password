from app.main import check_password


def test_all_rules() -> None:
    assert check_password("Pass@word1") is True


def test_without_upp() -> None:
    assert check_password("pass@word1") is False


def test_longer_than_16() -> None:
    assert check_password("Saqwe1@rtunkjlsunk") is False


def test_too_short() -> None:
    assert check_password("Sho1@") is False


def test_without_digit() -> None:
    assert check_password("Pass@word") is False


def test_without_special() -> None:
    assert check_password("Pass1word") is False

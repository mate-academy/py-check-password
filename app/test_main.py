from app.main import check_password


def test_password_length_min() -> None:
    assert check_password(password="drW321@") is False


def test_password_length_max() -> None:
    assert check_password(password="DFGKkwfmwk23234!@#") is False


def test_password_symbols() -> None:
    assert check_password(password="Aіке2345!") is False


def test_password_conditions() -> None:
    assert check_password(password="Svit2307@")

from app.main import check_password


def test_only_latter() -> None:
    assert check_password("PaZd") is False
    assert check_password("Password1") is False
    assert check_password("Password1@") is True


def test_min_and_max_length() -> None:
    assert check_password("Rd1@") is False
    assert check_password("Password1@") is True
    assert check_password("Rd1@se2514piv4!!k") is False


def test_without_digits() -> None:
    assert check_password("Pass@wordh") is False


def test_one_upper_letter() -> None:
    assert check_password("pass@wordh1") is False
    assert check_password("Pass@wordh1") is True

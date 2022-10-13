from app.main import check_password


def test_not_in_right_range() -> None:
    assert check_password("Ge3$") is False


def test_has_not_first_upper_letter() -> None:
    assert check_password("g5kjgkfk$$") is False


def test_has_not_digit() -> None:
    assert check_password("Grunfke$djf") is False


def test_has_not_special() -> None:
    assert check_password("Gr5jgvjdi5") is False


def test_is_successful() -> None:
    assert check_password("Pass@word1") is True


def test_password_is_too_long() -> None:
    assert check_password("R111111111111111111111$") is False

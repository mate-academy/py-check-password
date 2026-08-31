from app.main import check_password


def test_should_check_min_length() -> None:
    assert check_password("Pa@wod1") is False


def test_should_check_max_length() -> None:
    assert check_password("Pass@word122222222") is False


def test_should_check_has_digit() -> None:
    assert check_password("Pass@word") is False


def test_should_check_has_upper_case_letter() -> None:
    assert check_password("pass@word1") is False


def test_should_check_has_special_symbol() -> None:
    assert check_password("Pass~word1") is False

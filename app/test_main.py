from app.main import check_password


def test_password_not_match_min_length() -> None:
    assert check_password("Mima8@") is False


def test_password_not_match_max_length() -> None:
    assert check_password("Mima_hen_chang_1@1") is False


def test_password_has_no_uppercase_letter() -> None:
    assert check_password("pass@word1") is False


def test_password_has_no_digit() -> None:
    assert check_password("Pass@word") is False


def test_password_has_no_special_character() -> None:
    assert check_password("Password1") is False


def test_valid_password_meets_all_rules() -> None:
    assert check_password("Pass@word1") is True

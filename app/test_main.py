from app.main import check_password


def test_check_correct_password_have_to_be_true() -> None:
    assert (
        check_password("Pass@word1") is True
    ), "Is correct password have to be true"


def test_check_length_of_password_short_have_to_be_false() -> None:
    assert (
        check_password("Str@n1") is False
    ), "check length of password. It is short have to be false"


def test_check_length_of_password_long_have_to_be_false() -> None:
    assert (
        check_password("Str@n1Str@n1Str@n1") is False
    ), "check length of password. It is long have to be false"


def test_check_apper_case_letter_in_password_have_to_be_false() -> None:
    assert (
        check_password("q@1ertyuiop") is False
    ), "check apper case letter in password have to be false"


def test_check_simbols_in_password_have_to_be_false() -> None:
    assert (
        check_password("qW1ertyuiop") is False
    ), "check simbols in simbols of password have to be false"


def test_check_figures_in_password_have_to_be_false() -> None:
    assert (
        check_password("qW@ertyuiop") is False
    ), "check figures in simbols of password have to be false"

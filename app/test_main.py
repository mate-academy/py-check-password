from app.main import check_password


def test_correct_password() -> None:
    assert (check_password("Pass@word1") is True),\
        "Correct password, should be True"


def test_less_than_8() -> None:
    assert (check_password("Ps@d1") is False), \
        "Password is less than 8 symbols"


def test_more_than_16() -> None:
    assert (
           check_password("Pass@word1sfdsdfsfsdfs") is False
           ), "Password is more than 16 symbols"


def test_dont_has_digit() -> None:
    assert (
           check_password("Pass@worfdfd") is False
           ), "Password should have at least one digit"


def test_dont_has_special_symbol() -> None:
    assert (
           check_password("Passw2orfdfd") is False
           ), "Password should have special symbols"


def test_dont_has_upper_letter() -> None:
    assert (
           check_password("e5ass@worfdfd") is False
           ), "Password should have at least one upper letter"

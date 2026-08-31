from .main import check_password


def test_base_passwords() -> None:
    for password, value in {"Pass@word1": True,
                            "qwerty": False, "Password@@": False}.items():
        assert check_password(password) is value


def test_check_short_length() -> None:
    assert check_password("Pas1@") is False


def test_check_long_length() -> None:
    assert check_password("Passwordpsasaijiayiyasidaosid1@") is False


def test_check_without_uppercase() -> None:
    assert check_password("qwertyqwert1@") is False


def test_check_without_special() -> None:
    assert check_password("Password222") is False


def test_check_without_digits() -> None:
    assert check_password("Password@@") is False

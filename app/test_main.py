from app.main import check_password


def test_for_too_short_password():
    assert check_password("Passw_1") is False, (
        "Password should contain minimum 8 characters.")


def test_for_too_long_password():
    assert check_password("Password_test1970") is False, (
        "Password should contain maximum 16 characters.")


def test_should_contain_upper_letter():
    assert check_password("password_test1") is False, (
        "Password should contain at least 1 upper character.")


def test_should_contain_digit():
    assert check_password("Password_test") is False, (
        "Password should contain at least 1 digit.")


def test_should_contain_special_character():
    assert check_password("Passwordtest1") is False, (
        "Password should contain at least 1 special character.")

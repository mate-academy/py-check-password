from app.main import check_password


def test_password_have_at_least_8_characters():
    assert check_password("Rwe8ke!") is False


def test_password_have_less_than_17_characters():
    assert check_password("rwe$ikEe4rff23r45") is False


def test_password_should_have_at_least_1_upper_letter():
    assert check_password("dsf8sdf@fff") is False


def test_password_should_have_at_least_1_digit():
    assert check_password("dsTsdf!ffe") is False


def test_password_should_have_at_least_1_special():
    assert check_password("d8sfsdfRffy") is False

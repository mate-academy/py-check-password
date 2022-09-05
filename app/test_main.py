from app.main import check_password


def test_password_right():
    password = check_password("NewBrunswick73!@")
    assert password


def test_7_char():
    password = check_password("Cana73!")
    assert password is False


def test_17_char():
    password = check_password("NewBrunswick73!@K")
    assert password is False


def test_no_upper():
    password = check_password("canada73!")
    assert password is False


def test_no_digit():
    password = check_password("New_canada!")
    assert password is False


def test_no_special_char():
    password = check_password("canada73")
    assert password is False


def test_empty_string():
    password = check_password("")
    assert password is False

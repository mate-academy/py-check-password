from app.main import check_password


def test_for_invalid_characters() -> None:
    assert not check_password("Asdf1234%")


def test_for_number_of_characters_more_than_the_maximum() -> None:
    assert not check_password("Awsedrf123456789$")


def test_for_number_of_characters_less_than_minimum() -> None:
    assert not check_password("Asdf12$")


def test_on_the_absence_of_numbers() -> None:
    assert not check_password("Asdfghj$")


def test_for_the_absence_of_the_character() -> None:
    assert not check_password("Asdfghj123456789")


def test_on_the_absence_of_a_capital_letter() -> None:
    assert not check_password("123456789$")


def test_password_in_compliance() -> None:
    assert check_password("Asdf12345$")

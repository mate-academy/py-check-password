from app.main import check_password


def test_correct_password() -> None:
    password = "Pass@word1"
    expected_outdated = True
    assert check_password(password) == expected_outdated


def test_wrong_password() -> None:
    password = "qwerty"
    expected_outdated = False
    assert check_password(password) == expected_outdated


def test_long_password() -> None:
    password = "ThisIsAVeryLongPassword123!@#"
    expected_outdated = False
    assert check_password(password) == expected_outdated


def test_short_password() -> None:
    password = "Ab1!"
    expected_outdated = False
    assert check_password(password) == expected_outdated


def test_no_capitals_password() -> None:
    password = "password123!@#"
    expected_outdated = False
    assert check_password(password) == expected_outdated


def test_without_numbers_password() -> None:
    password = "Password!@#"
    expected_outdated = False
    assert check_password(password) == expected_outdated


def test_special_characters_password() -> None:
    password = "Password123"
    expected_outdated = False
    assert check_password(password) == expected_outdated

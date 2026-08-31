from app.main import check_password


def test_less_than_8_characters() -> None:
    assert check_password("Test_1") is False


def test_equal_to_8_characters() -> None:
    assert check_password("Test_123") is True


def test_equal_to_16_characters() -> None:
    assert check_password("Test_test_12345!") is True


def test_more_than_16_characters() -> None:
    assert check_password("Test_test_12345!!!") is False


def test_without_upper_letter() -> None:
    assert check_password("test_123@") is False


def test_without_special_character() -> None:
    assert check_password("Testtest123") is False


def test_without_digits() -> None:
    assert check_password("Test_test#") is False


def test_with_not_allowed_special_characters() -> None:
    assert check_password("Test~test1") is False

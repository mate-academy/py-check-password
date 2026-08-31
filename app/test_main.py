import unittest
from app.main import check_password


class PasswordCheckerTests(unittest.TestCase):
    def test_valid_password(self) -> None:
        self.assertTrue(check_password("Pass@word1"))

    def test_password_too_short(self) -> None:
        self.assertFalse(check_password("qwerty"))

    def test_password_no_special_character(self) -> None:
        self.assertFalse(check_password("Strng123"))

    def test_password_no_uppercase_letter(self) -> None:
        self.assertFalse(check_password("str@ng123"))

    def test_password_no_digit(self) -> None:
        self.assertFalse(check_password("String@word"))

    def test_password_invalid_character(self) -> None:
        self.assertFalse(check_password("Pass@word!"))

    def test_password_too_long(self) -> None:
        self.assertFalse(check_password("Password12345678901"))

    def test_should_check_max_length(self) -> None:
        self.assertFalse(check_password("Pass@word123456789"))

    def test_should_check_min_length(self) -> None:
        self.assertFalse(check_password("Pass@w1"))


if __name__ == "__main__":
    unittest.main()

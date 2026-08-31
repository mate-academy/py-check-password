import unittest
from app.main import check_password


class TestCheckPassword(unittest.TestCase):

    def test_valid_password(self) -> None:
        self.assertTrue(check_password("Pass@word1"))

    def test_invalid_length_short(self) -> None:
        self.assertFalse(check_password("Short@1"))

    def test_invalid_length_long(self) -> None:
        self.assertFalse(check_password("Pass@word1wwwwwww"))

    def test_invalid_no_digit(self) -> None:
        self.assertFalse(check_password("NoDigit@Special"))

    def test_invalid_no_special_char(self) -> None:
        self.assertFalse(check_password("NoSpecialChar123"))

    def test_invalid_no_uppercase(self) -> None:
        self.assertFalse(check_password("nouppercase@123"))

    def test_invalid_invalid_char(self) -> None:
        self.assertFalse(check_password("InvalidChar$"))

    def test_invalid_multiple_special_chars(self) -> None:
        self.assertFalse(check_password("TooManySpecialChars@!"))

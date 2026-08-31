import unittest
from app.main import check_password


class TestCheckPassword(unittest.TestCase):

    def test_valid_password(self) -> None:
        self.assertTrue(check_password("Pass@word1"))
        self.assertTrue(check_password("Strong$Pass2"))

    def test_too_short_password(self) -> None:
        self.assertFalse(check_password("Short1!"))
        self.assertFalse(check_password("1234567"))

    def test_too_long_password(self) -> None:
        self.assertFalse(check_password("ThisPasswordIsWayTooLong1!"))
        self.assertFalse(check_password("A" * 17 + "1!"))

    def test_missing_special_character(self) -> None:
        self.assertFalse(check_password("Password1"))
        self.assertFalse(check_password("Passw0rd"))

    def test_missing_digit(self) -> None:
        self.assertFalse(check_password("Password!"))
        self.assertFalse(check_password("Password@"))

    def test_missing_uppercase_letter(self) -> None:
        self.assertFalse(check_password("password1!"))
        self.assertFalse(check_password("12345678@"))

    def test_valid_special_characters(self) -> None:
        self.assertTrue(check_password("Valid1$Password"))
        self.assertTrue(check_password("Good@Pass2"))

    def test_invalid_characters(self) -> None:
        self.assertFalse(check_password("Invalid!Password#"))
        self.assertFalse(check_password("Password_with_space 1!"))

import unittest
from .main import check_password


class TestCheckPassword(unittest.TestCase):
    def test_valid_passwords(self) -> None:
        self.assertTrue(check_password("Pass@word1"))
        self.assertTrue(check_password("Strong#Pass2"))

    def test_short_passwords(self) -> None:
        self.assertFalse(check_password("Aa@1"))

    def test_long_passwords(self) -> None:
        self.assertFalse(check_password("LongerThanSixteenChars1$"))

    def test_no_digit(self) -> None:
        self.assertFalse(check_password("Password@"))

    def test_no_special_character(self) -> None:
        self.assertFalse(check_password("Password1"))

    def test_no_uppercase_letter(self) -> None:
        self.assertFalse(check_password("password1@"))

    def test_invalid_characters(self) -> None:
        self.assertFalse(check_password("Pass*word1"))
        self.assertFalse(check_password("Pass^word2"))


if __name__ == "__main__":
    unittest.main()

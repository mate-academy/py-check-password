import unittest
from app.main import check_password


class TestCheckPassword(unittest.TestCase):
    def test_valid_password(self) -> None:
        self.assertTrue(check_password("Pass@word1"))

    def test_invalid_password_too_short(self) -> None:
        self.assertFalse(check_password("P@w1"))

    def test_invalid_password_no_digit(self) -> None:
        self.assertFalse(check_password("Pass@word"))

    def test_invalid_password_no_special_char(self) -> None:
        self.assertFalse(check_password("Password1"))

    def test_invalid_password_no_uppercase(self) -> None:
        self.assertFalse(check_password("pass@word1"))

    def test_invalid_password_non_latin_chars(self) -> None:
        self.assertFalse(check_password("パスワード1@"))

    def test_invalid_password_too_long(self) -> None:
        self.assertFalse(check_password("ThisIsTooLongPassword@1"))


if __name__ == "__main__":
    unittest.main()

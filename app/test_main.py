import unittest
from app.main import check_password


class TestCheckPassword(unittest.TestCase):
    def test_valid_password(self) -> None:
        self.assertTrue(check_password("Pass@word1"),
                        "Valid password is not "
                        "recognized correctly")

    def test_password_too_short(self) -> None:
        self.assertFalse(check_password("P@ss1"),
                         "Password that is too "
                         "short should be invalid")

    def test_password_too_long(self) -> None:
        self.assertFalse(check_password("P@ssword1toolongforthis"),
                         "Password that is too "
                         "long should be invalid")

    def test_password_missing_digit(self) -> None:
        self.assertFalse(check_password("Password@"),
                         "Password missing a digit "
                         "should be invalid")

    def test_password_missing_special_char(self) -> None:
        self.assertFalse(check_password("Password1"),
                         "Password missing a special "
                         "character should be invalid")

    def test_password_missing_uppercase(self) -> None:
        self.assertFalse(check_password("pass@word1"),
                         "Password missing an uppercase "
                         "letter should be invalid")

    def test_password_with_invalid_char(self) -> None:
        self.assertFalse(check_password("Pass@word1?"),
                         "Password with an invalid "
                         "character should be invalid")

    def test_password_only_allowed_special_chars(self) -> None:
        self.assertTrue(check_password("Pass1@-_$"),
                        "Password with only allowed special "
                        "characters should be valid")

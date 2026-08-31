import unittest
from app.main import check_password


class TestPassword(unittest.TestCase):
    def test_digit(self) -> None:
        self.assertTrue(check_password("password123!A"))

    def test_no_digit(self) -> None:
        self.assertFalse(check_password("password!A"))

    def test_check_exceeding_length(self) -> None:
        self.assertFalse(check_password("A#23456789012345678ll"))

    def test_check_uppercase_char(self) -> None:
        self.assertTrue(check_password("password123!A"))

    def test_check_uppercase_char_missing(self) -> None:
        self.assertFalse(check_password("password123!"))

    def check_min_length(self) -> None:
        self.assertTrue(check_password("Pas1w!rd"))

    def test_check_short_length(self) -> None:
        self.assertFalse(check_password("Pa$1"))

    def test_check_special_character(self) -> None:
        self.assertTrue(check_password("password123A!"))

    def test_check_no_special_character(self) -> None:
        self.assertFalse(check_password("password123A"))

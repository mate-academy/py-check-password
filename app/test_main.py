import unittest

from app.main import check_password


class TestCheckPassword(unittest.TestCase):

    def test_less_than_8_characters(self) -> None:
        self.assertFalse(check_password("qwerT@1"))

    def test_more_than_16_characters(self) -> None:
        self.assertFalse(check_password("qwertyqwertyqw1@A"))

    def test_without_special_character(self) -> None:
        self.assertFalse(check_password("qwerty1A"))

    def test_without_digits(self) -> None:
        self.assertFalse(check_password("qwertyA@"))

    def test_without_uppercase_letter(self) -> None:
        self.assertFalse(check_password("qwerty1@"))

    def test_should_return_true_if_password_is_correct(self) -> None:
        self.assertTrue(check_password("qwertY1@"))

import unittest

from app.main import check_password


class TestCheckPassword(unittest.TestCase):

    def test_valid_password(self) -> None:
        self.assertTrue(check_password("Pass@word1"))

    def test_invalid_passwords(self) -> None:
        invalid_passwords = {
            "Str@ng": False,
            "Password1": False,
            "qwerty": False,
            "pass@word": False,
            "PASSWORD1": False,
            "Pass1234": False,
            "12345678": False,
            "Short!1": False,
            "@@@@!!!!": False,
            "Valid@PasswordThatIsWayTooLong1": False
        }

        for password, expected in invalid_passwords.items():
            with self.subTest(password=password):
                self.assertEqual(check_password(password), expected)

    def test_boundary_values(self) -> None:
        self.assertTrue(check_password("Pass@w1rd"))
        self.assertTrue(check_password("Valid@Pass1234"))

    def test_should_check_digit(self) -> None:
        invalid_passwords = [
            "Pass@word",
            "Valid@Pass",
            "Upper@Letter"
        ]
        for password in invalid_passwords:
            with self.subTest(password=password):
                self.assertFalse(check_password(password))

    def test_should_check_upper_letter(self) -> None:
        invalid_passwords = [
            "pass@word1",
            "valid@1234",
            "special@!2"
        ]
        for password in invalid_passwords:
            with self.subTest(password=password):
                self.assertFalse(check_password(password))


if __name__ == "__main__":
    unittest.main()

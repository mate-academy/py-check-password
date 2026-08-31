import unittest
from app.main import check_password


class TestCheckPassword(unittest.TestCase):
    def assert_check_password(
            self,
            password: str,
            expected_result: bool
    ) -> None:
        self.assertEqual(check_password(password), expected_result)

    def test_valid_password(self) -> None:
        self.assert_check_password("Pass@word1", True)

    def test_invalid_length_short(self) -> None:
        self.assert_check_password("abc", False)

    def test_invalid_length_long(self) -> None:
        self.assert_check_password("abcdefghijklmnopqrstuvwxyz", False)

    def test_invalid_no_digit(self) -> None:
        self.assert_check_password("Password@", False)

    def test_invalid_no_special_character(self) -> None:
        self.assert_check_password("Password1", False)

    def test_invalid_no_uppercase(self) -> None:
        self.assert_check_password("password@1", False)

    def test_invalid_non_ascii_character(self) -> None:
        self.assert_check_password("Pass@wórd1", False)

    def test_invalid_multiple_uppercase(self) -> None:
        self.assert_check_password("PASS@WORD1", True)

    def test_invalid_special_character(self) -> None:
        self.assert_check_password("Pass!word1", True)

    def test_invalid_special_character_multiple(self) -> None:
        self.assert_check_password("Pass@#word!1", True)

    def test_valid_maximum_length(self) -> None:
        self.assert_check_password("aB1$" + "a" * 10, True)

    def test_invalid_exceed_maximum_length(self) -> None:
        self.assert_check_password("aB1$" + "a" * 11, True)

    def test_valid_minimum_length(self) -> None:
        self.assert_check_password("aB1$abc", False)

    def test_invalid_exceed_minimum_length(self) -> None:
        self.assert_check_password("aB1$ab", False)

    def test_valid_boundary_length(self) -> None:
        self.assert_check_password("aB1$" + "a" * 8, True)

    def test_invalid_boundary_length_short(self) -> None:
        self.assert_check_password("aB1$" + "a" * 7, True)

    def test_invalid_boundary_length_long(self) -> None:
        self.assert_check_password("aB1$" + "a" * 17, False)


if __name__ == "__main__":
    unittest.main()

import unittest
from app.main import check_password


class TestCheckPassword(unittest.TestCase):

    def test_valid_password(self) -> None:
        self.assertTrue(check_password("Pass@word1"))
        self.assertTrue(check_password("TEST123!test"))
        self.assertTrue(check_password("A1!bcdefgh"))
        self.assertTrue(check_password("Valid123!pass"))

    def test_too_short(self) -> None:
        self.assertFalse(check_password("qwerty"))
        self.assertFalse(check_password("A1!bcde"))
        self.assertFalse(check_password(""))
        self.assertFalse(check_password("Ab1!"))

    def test_too_long(self) -> None:
        self.assertFalse(check_password("A1!bcdefghijklmno"))
        self.assertFalse(check_password("ThisIsAVeryLongPassword123!"))
        self.assertFalse(check_password("A1!" + "a" * 15))

    def test_no_uppercase(self) -> None:
        self.assertFalse(check_password("password123!"))
        self.assertFalse(check_password("alllowercase123!"))
        self.assertFalse(check_password("12345678!"))

    def test_no_digit(self) -> None:
        self.assertFalse(check_password("Password!"))
        self.assertFalse(check_password("NODIGITS_HERE"))
        self.assertFalse(check_password("OnlyLettersAnd!"))

    def test_no_special_char(self) -> None:
        self.assertFalse(check_password("Password123"))
        self.assertFalse(check_password("TEST123test"))
        self.assertFalse(check_password("OnlyLetters123"))

    def test_invalid_special_chars(self) -> None:
        self.assertFalse(check_password("Password123%"))
        self.assertFalse(check_password("Pass*word1"))
        self.assertFalse(check_password("Pass(word1"))
        self.assertFalse(check_password("Pass)word1"))

    def test_non_latin_letters(self) -> None:
        self.assertFalse(check_password("Passwörd1!"))
        self.assertFalse(check_password("Привет123!"))
        self.assertFalse(check_password("Pass字1!"))

    def test_boundary_lengths(self) -> None:
        self.assertTrue(check_password("A1!bcdef"))
        self.assertTrue(check_password("Ab1!cdef"))
        self.assertTrue(check_password("A1!" + "a" * 5))
        self.assertTrue(check_password("A1!bcdefghijklmn"))

    def test_exact_requirements(self) -> None:
        self.assertTrue(check_password("Abcdefg1!"))
        self.assertTrue(check_password("A1234567!"))
        self.assertTrue(check_password("A!2345678"))

    def test_multiple_of_each_type(self) -> None:
        self.assertTrue(check_password("ABCdef123!!!"))
        self.assertTrue(check_password("TEST123!test456@"))
        self.assertTrue(check_password("Aa1!Bb2@Cc3#"))

    def test_edge_cases(self) -> None:
        self.assertFalse(check_password("        "))
        self.assertFalse(check_password("\t\n\r"))
        self.assertFalse(check_password("PASSWORD"))
        self.assertFalse(check_password("12345678"))
        self.assertFalse(check_password("!!!!!!!!"))
        self.assertFalse(check_password("AaBbCcDd"))
        self.assertFalse(check_password("A1!A1!A"))

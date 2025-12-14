from app.main import check_password
from unittest import TestCase


class TestCheckPassword(TestCase):
    def test_correct(self) -> None:
        assert check_password("Pass@word1")

    def test_wrong_letters(self) -> None:
        assert not check_password("<PASSWORD>")

    def test_wrong_quantity_ge_16(self) -> None:
        assert not check_password("Pass@word1Pass@word1")

    def test_wrong_quantity_le_8(self) -> None:
        assert not check_password("Pas@w1")

    def test_only_lower(self) -> None:
        assert not check_password("pass@word1")

    def test_without_digits(self) -> None:
        assert not check_password("Pass@word")

    def test_without_spec(self) -> None:
        assert not check_password("Password1")

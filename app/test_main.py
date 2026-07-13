from app.main import check_password


class TestCheckPassword:
    def test_valid_password(self) -> None:
        assert check_password("Pass@word1") is True

    def test_too_short(self) -> None:
        assert check_password("Pass@1") is False

    def test_too_long(self) -> None:
        assert check_password("Pass@word1234567") is False

    def test_no_uppercase(self) -> None:
        assert check_password("pass@word1") is False

    def test_no_digit(self) -> None:
        assert check_password("Pass@word") is False

    def test_no_special_char(self) -> None:
        assert check_password("Password1") is False

    def test_invalid_characters(self) -> None:
        assert check_password("Pass@word1!") is False

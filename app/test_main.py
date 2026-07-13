from app.main import check_password


class TestCheckPassword:
    def test_valid_password(self):
        assert check_password('Pass@word1') is True

    def test_too_short(self):
        assert check_password('Pass@1') is False

    def test_too_long(self):
        assert check_password('Pass@word123456') is False

    def test_no_uppercase(self):
        assert check_password('pass@word1') is False

    def test_no_digit(self):
        assert check_password('Pass@word') is False

    def test_no_special_char(self):
        assert check_password('Password1') is False

    def test_invalid_characters(self):
        assert check_password('Pass@word1!') is False

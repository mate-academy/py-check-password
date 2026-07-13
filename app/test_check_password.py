from app.main import check_password


class TestCheckPassword:
    @staticmethod
    def test_invalid_characters():
        assert check_password('Pass@word1!') is False

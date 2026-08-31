import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize("password, expected", [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ngpassword123456", False),
        ("Пароль12345@@", False),
        ("", False)
    ])
    def test_check_password(self, password: str, expected: bool) -> None:
        result = check_password(password)

        assert result == expected

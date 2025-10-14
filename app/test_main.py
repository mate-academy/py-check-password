import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password,expected",
        [
            ("Pass@word1", True),
            ("Good#Pass9", True),
            ("qwerty", False),
            ("Str@ng", False),
            ("password1", False),
            ("PASSWORD1", False),
            ("Pass word1@", False),
            ("Пароль@1", False),
            ("Abcdef1$", True),
            ("A1b2C3d4E5f6G7h8!", False),
            ("A1b2C3d4E5f6G7h8!9", False),
        ]
    )
    def test_check_password(self, password: str, expected: bool) -> None:
        assert check_password(password) == expected

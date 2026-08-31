from app.main import check_password
import pytest


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, is_result",
        [
            ("Pass@word1", True),
            ("qwerty", False),
            ("Str@ng", False),
            ("Qwertyytrewq", False),
            ("Qwerty1234", False),
            ("qwerty1234", False),
            ("Pass@1", False),
            ("Pass@word11243124rsdfegherh", False),
            ("Pass@words", False),
            ("pass@word1", False),
        ]
    )
    def test_check_password(
            self,
            password: str,
            is_result: bool
    ) -> None:
        assert check_password(password) is is_result

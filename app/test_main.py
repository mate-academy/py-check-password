import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, expected_result",
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
    def test_check_password(self,
                            password: str,
                            expected_result: bool) -> None:
        assert check_password(password) is expected_result

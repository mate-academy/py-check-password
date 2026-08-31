import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password,result",
        [
            ("Pass@word1", True),
            ("Pass@word1234567", True),
            ("passw", False),
            ("P@ssw1", False),
            ("password", False),
            ("P@ssword", False),
            ("Password1", False),
            ("password1", False),
            ("pass@word1", False),
            ("Pass@word12345678", False),
        ]
    )
    def test_check_password(self, password: str, result: bool) -> None:
        assert check_password(password) == result

import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, result",
        [
            ("qw!z4rE", False),
            ("qwertyIstoolon!gpas85sword", False),
            ("qw5erty!#", False),
            ("Pass@!word", False),
            ("Pas99leg", False),
        ]
    )
    def test_check_password(self, password, result):
        assert check_password(password) == result

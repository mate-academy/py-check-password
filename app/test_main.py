import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, result",
        [
            pytest.param("Pass@word1", True,
                         id="password with digits, symbols and upper letter"),
            pytest.param("qwerty", False,
                         id="only letters in lower register"),
            pytest.param("Pass@word", False,
                         id="password without digits"),
            pytest.param("Ps@wd1", False,
                         id="too short password"),
            pytest.param("Pas#####s@wor111222d", False,
                         id="too long password"),
            pytest.param("Password1", False,
                         id="password without special symbol"),
            pytest.param("pass@word1", False,
                         id="password without upper letter")
        ]
    )
    def test_check_password(self, password, result):
        assert check_password(password) == result

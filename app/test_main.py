import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, result",
        [pytest.param("Pass@word11023495", False,
                      id="Password too long"),
         pytest.param("pass@word1", False,
                      id="Password  without uppercase letter"),
         pytest.param("Password1", False,
                      id="Password  without special symbols"),
         pytest.param("Pas@swords", False,
                      id="Password  without digits"),
         pytest.param("Pa@s1", False,
                      id="Password too short"),
         ])
    def test_check_password(self, password: str, result: bool) -> None:
        assert check_password(password) == result

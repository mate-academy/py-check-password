from app.main import check_password
import pytest


class TestPassword:

    @pytest.mark.parametrize(
        "password,result",
        [
            pytest.param('Pass@word1', True,
                         id="password is valid"),
            pytest.param("C@t1", False,
                         id="Password is too short"),
            pytest.param("P@sswordistoolong18", False,
                         id="Password is too long"),
            pytest.param("password@123", False,
                         id="Password has no capital letter"),
            pytest.param("Password123", False,
                         id="Password has no special character"),
            pytest.param("P@ssword", False,
                         id="Password has no digits"),
        ]
    )
    def test_password(self, password, result):
        assert check_password(password) == result

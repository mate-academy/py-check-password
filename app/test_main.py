from app.main import check_password
import pytest


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, result",
        [
            pytest.param(
                "Abcd12@",
                False,
                id="Too short password"
            ),
            pytest.param(
                "Abcd@123456789101112314",
                False,
                id="Too long password"
            ),
            pytest.param(
                "$@#&cde1234",
                False,
                id="No one uppercase letter"
            ),
            pytest.param(
                "Abcde1234",
                False,
                id="No one special symbol"
            ),
            pytest.param(
                "Abcd$@#&",
                False,
                id="No one digit"
            ),
            pytest.param(
                "Abcd$@#123+4",
                False,
                id="If forbidden symbol in password"
            ),
            pytest.param(
                "Abcd$@#1234",
                True,
                id="Password is valid"
            )
        ]
    )
    def test_check_password(
            self,
            password,
            result
    ):
        assert check_password(password) == result

import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, result",
        [
            (
                "Pass@word1",
                True,
            ),
            pytest.param(
                "Qwe@1",
                False,
                id="password short, need more symbols"

            ),
            pytest.param(
                "P@ssword",
                False,
                id="Password should contain at least 1 digit"
            ),
            pytest.param(
                "P@assword1qwerttyas",
                False,
                id="Password too long should be less symbols"
            ),
            pytest.param(
                "pass@word1",
                False,
                id="password should start with UpperCase letter"
            ),
            pytest.param(
                "Password1",
                False,
                id="Password should contain at least 1 special symbol"
            )
        ]
    )
    def test_check_password(
            self,
            password: str,
            result: bool
    ) -> None:
        assert check_password(password) == result

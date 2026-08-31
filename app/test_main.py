import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, result",
        [
            pytest.param(
                "Pass@word1",
                True,
                id="Correct password"
            ),
            pytest.param(
                "Pass@1",
                False,
                id="Password is too short"
            ),
            pytest.param(
                "Pass@word111111111",
                False,
                id="Password is too long"
            ),
            pytest.param(
                "Pass@word",
                False,
                id="Password should contain at least 1 digit"
            ),
            pytest.param(
                "Password1111",
                False,
                id="Password should contain at least 1 special symbol"
            ),
            pytest.param(
                "pass@word1",
                False,
                id="Password should contain at least 1 uppercase letter "
            )
        ]
    )
    def test_check_password(
            self,
            password: str,
            result: bool
    ) -> None:
        assert check_password(password) == result

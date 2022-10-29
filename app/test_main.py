from app.main import check_password
import pytest


class TestCheckPassword:
    @pytest.mark.parametrize(
        "expected_password,expected_result",
        [
            pytest.param(
                "Password1",
                False,
                id="passwords needs to be without without special symbols"
            ),
            pytest.param(
                "Pass@w1",
                False,
                id="password is too short"
            ),
            pytest.param(
                "Pass@word",
                False,
                id="password needs to be without digits"
            ),
            pytest.param(
                "Pass@wordPass@word1",
                False,
                id="the password is too long"
            ),
            pytest.param(
                "Pass@word1",
                True,
                id="all checks are done correctly"
            ),
            pytest.param(
                "pass@word1",
                False,
                id="password needs to be without upper letters"
            )
        ]
    )
    def test_check_password(
            self,
            expected_password: str,
            expected_result: bool
    ) -> None:
        assert check_password(expected_password) == expected_result

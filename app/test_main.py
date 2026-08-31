import pytest

from app.main import check_password


class TestPassword:
    @pytest.mark.parametrize(
        "password, result",
        [
            pytest.param(
                "1$P",
                False,
                id="Password should be at least 8 characters long"
            ),
            pytest.param(
                "1$PzzXjddsk232PZ!",
                False,
                id="Password should be maximum 16 characters long"
            ),
            pytest.param(
                "Pass^word1",
                False,
                id="Should accept only special character from `$@#&!-_`"
            ),
            pytest.param(
                "pass$word1",
                False,
                id="Should contains at least 1 uppercase letter"
            ),
            pytest.param(
                "Password12",
                False,
                id="Should contains at least 1 special character"
            ),
            pytest.param(
                "Passw@ordiX",
                False,
                id="Should contains at least 1 number"
            ),
            pytest.param(
                "Pass@word1",
                True,
                id="Password should pass all restrictions"
            )
        ]
    )
    def test_password_validator_works_correctly(
            self,
            password: str,
            result: bool
    ) -> None:
        assert check_password(password) == result

import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, "
        "expected_result", [
            pytest.param(
                "Pass@word1password",
                False,
                id="Tests should returns False for too long passwords"
            ),
            pytest.param(
                "Pass@r7",
                False,
                id="Tests should returns False for short passwords"
            ),
            pytest.param(
                "Pass@wordd",
                False,
                id="Tests should returns False for passwords without digits "
            ),
            pytest.param(
                "Passsword9",
                False,
                id="Tests should returns False for passwords "
                   "without special symbols"
            ),
            pytest.param(
                "pass@word1",
                False,
                id="Tests should returns False for passwords "
                   "without uppercase letter"
            )
        ]
    )
    def test_check_password(
            self,
            password: str,
            expected_result: bool
    ) -> None:

        assert check_password(password) == expected_result

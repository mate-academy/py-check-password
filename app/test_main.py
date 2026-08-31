import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "initial_password,expected_result",
        [
            pytest.param(
                "Pass@word1",
                True,
                id="should check upper, special, digit"
            ),

            pytest.param(
                "qwerty1@",
                False,
                id="should check upper"
            ),

            pytest.param(
                "Str@ng",
                False,
                id="should check digit and length"
            ),

            pytest.param(
                "ddlgkk1@gllgllglglgllglglgAg",
                False,
                id="should check maximum length"
            ),

            pytest.param(
                "Ddf1@",
                False,
                id="should check minimum length"
            )

        ]
    )
    def test_understatnd_isogram_correctly(
            self,
            initial_password: str,
            expected_result: bool
    ) -> None:
        assert check_password(initial_password) == expected_result

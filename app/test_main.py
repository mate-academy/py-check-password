from app.main import check_password
import pytest


class TestCheckPassword:
    @pytest.mark.parametrize(
        "input_str, expected_result",
        [
            pytest.param(
                "Aa@",
                False
            ),
            pytest.param(
                "asdfgG@",
                False
            ),
            pytest.param(
                {"a": 2},
                False
            ),
            pytest.param(
                ["sss12Ssfre@2"],
                False
            ),
            pytest.param(
                "d123S@z",
                False
            ),
            pytest.param(
                "asdfgh1@#",
                False
            ),
            pytest.param(
                "asdfgH1@#",
                True
            ),
            pytest.param(
                "12345678912aS@df",
                True
            ),
            pytest.param(
                "12345678912aS@dff",
                False
            ),
            pytest.param(
                "qwerty@sq",
                False
            ),
            pytest.param(
                "qwertyu$@#&!-_",
                False
            ),
            pytest.param(
                "qwetyu$@#&!-_1",
                False
            ),
            pytest.param(
                "qweyu$@#&!-_1Q",
                True
            ),
            pytest.param(
                "qwertyYY12",
                False
            ),
            pytest.param(
                "qwerty@@Qq",
                False
            )
        ]
    )
    def test_correct_output(
            self,
            input_str: str,
            expected_result: bool
    ) -> None:
        assert check_password(input_str) == expected_result

    @pytest.mark.parametrize(
        "input_val, exp_error",
        [
            pytest.param(
                True,
                TypeError
            ),
            pytest.param(
                1,
                TypeError
            )
        ]
    )
    def test_correct_error(
            self,
            input_val: str,
            exp_error: Exception
    ) -> None:
        with pytest.raises(exp_error):
            check_password(input_val)

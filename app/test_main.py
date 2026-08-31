from app.main import check_password
import pytest


class TestCheckPassValidClass:
    @pytest.mark.parametrize(
        "password,result",
        [
            # too_short
            ("Sho@r1", False),
            # too long
            ("ewqwj11enq_jenqnwekjqnwkejnqGGekjqwnej", False),
            # no_upper_case
            ("pass@word1", False),
            # no_digits
            ("qwer@YY____", False),
            # no_special_symbols
            ("Symbol1sation", False),
            # ok
            ("Symbol1sati_n", True),
            # max_lenght
            ("ewqwj11enq_jFnqn", True)

        ],
    )
    def test_check_password_is_valid(self, password: str,
                                     result: bool) -> None:
        assert check_password(password) == result

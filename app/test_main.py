import pytest

from app.main import check_password


class TestCheckPassword:

    @pytest.mark.parametrize(
        "password,expected_result",
        [
            ("AaZa_55Y", True),
            ("R$@#&!-_99", True),
            pytest.param(
                "AaПa_55Y", False,
                id="invalid alphabet character"
            ),
            pytest.param(
                "AaZa_%5Y", False,
                id="invalid special character"
            ),
            pytest.param(
                "AaZ_5", False,
                id="should be at least 8 characters"
            ),
            pytest.param(
                "AaaaaZzzzza_55Yyyyy", False,
                id="should be maximum 16 characters"
            ),
            pytest.param(
                "Aaaa_zzY", False,
                id="should be contains at least 1 digit"
            ),
            pytest.param(
                "Aaaa5zzY", False,
                id="should be contains at least 1 special character"
            ),
            pytest.param(
                "a12345678z", False,
                id="should be contains at least 1 uppercase letter"
            ),
            pytest.param(
                "12345678", False,
                id="should be contains at special character and letter"
            ),
            pytest.param(
                "abcdefjg", False,
                id="should be contains at special character and digit"
            ),
            pytest.param(
                "$@#&!-_$", False,
                id="should be contains at letter and digit"
            ),
        ]
    )
    def test_check_password(
            self,
            password: str,
            expected_result: bool
    ) -> None:

        assert check_password(password) == expected_result

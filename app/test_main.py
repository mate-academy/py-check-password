import pytest

from app.main import check_password


class TestCorrectExpected:
    @pytest.mark.parametrize(
        "password,expected_result",
        [
            pytest.param(
                "Pass@word1",
                True,
                id="Check all requirements"
            ),
            pytest.param(
                "Q1_rtyu",
                False,
                id="password must be more 8 characters"
            ),
            pytest.param(
                "Q1_rtyuiopqwertyy",
                False,
                id="password must be less 16 characters"
            ),
            pytest.param(
                "Q1qrtyuio",
                False,
                id="password must be have special character"
            ),
            pytest.param(
                "Qr_qrtyuio",
                False,
                id="password must be have greater than one digit"
            ),
            pytest.param(
                "q1_qrtyuio",
                False,
                id="password must be have uppercase letter"
            ),

        ]
    )
    def test_check_password(self, password: str,
                            expected_result: bool) -> None:
        assert check_password(password) == expected_result

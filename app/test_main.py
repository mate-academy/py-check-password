import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password,expected",
        [
            pytest.param(
                "Pass@word1", True,
                id="Good pass practise"
            ),
            pytest.param(
                "qwerty", False,
                id="Has no digits, special chars, and uppercase letters"
            ),
            pytest.param(
                "Short1@", False,
                id="Less than 8 chars long"
            ),
            pytest.param(
                "VeryLooongPassword1@", False,
                id="More than 16 chars"
            ),
            pytest.param(
                "nouppercase1@", False,
                id="Has no uppercase letters"
            ),
            pytest.param(
                "NoSpecialSymbol1", False,
                id="Has no special symbols from allowed set"
            ),
            pytest.param(
                "NoDigits@!", False,
                id="No digits"
            ),
        ]
    )
    def test_check_password(
            self,
            password: str,
            expected: bool
    ) -> None:
        assert check_password(password) == expected

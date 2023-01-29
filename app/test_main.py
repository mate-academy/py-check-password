from app.main import check_password
import pytest


class TestCheckPassword:

    @pytest.mark.parametrize(
        "password,expected_result",
        [
            pytest.param(
                "Pass@word1",
                True,
                id="should return True for a password with"
                   "1 digit, 1 special character, 1 uppercase letter"
            ),
            pytest.param(
                "qwerty@1",
                False,
                id="should return False for passwords without uppercase letter"
            ),
            pytest.param(
                "qwe4TyBh",
                False,
                id="should return False for passwords without special symbols"
            ),
            pytest.param(
                "Stra@ngy",
                False,
                id="should return False for passwords without digits"
            ),
            pytest.param(
                "Str@ng1",
                False,
                id="should return False when less than 8 characters"
            ),
            pytest.param(
                "Pass@word1Pass@word1Pass@word1",
                False,
                id="should return False when length exceeds 16 characters"
            ),
        ]
    )
    def test_check_password_correctly(
            self,
            password: str,
            expected_result: bool
    ) -> None:
        assert check_password(password) == expected_result

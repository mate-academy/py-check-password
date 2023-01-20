import pytest

from app.main import check_password


class TestChekPasswor:
    @pytest.mark.parametrize(
        "password_to_check, expected_result",
        [
            pytest.param(
                "Pass@word1",
                True,
                id="should return True when pwd is valid"
            ),
            pytest.param(
                "Pass@word12345677",
                False,
                id="should return False when pwd is too long"
            ),
            pytest.param(
                "Str@ng1",
                False,
                id="should return False when pwd is too short"
            ),
            pytest.param(
                "Qwertyuit1",
                False,
                id="should return False when no special symbols"
            ),
            pytest.param(
                "qw1ertyu@",
                False,
                id="should return False when no uppercase"
            ),
            pytest.param(
                "Password@",
                False,
                id="should return False when no digits"
            )
        ]
    )
    def test_check_password(
            self,
            password_to_check: str,
            expected_result: bool
    ) -> None:
        assert check_password(password_to_check) == expected_result

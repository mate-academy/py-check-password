from app.main import check_password

import pytest


class TestCheckPassword:
    @pytest.mark.parametrize(
        "input_password,expected_bool",
        [
            pytest.param("Qwe1rt!", False,
                         id="Password must be 8 to 16 characters"),
            pytest.param("Qwe1rt!Qwe1rt!Qwe", False,
                         id="Password must be 8 to 16 characters"),
            pytest.param("Pass@щword1", False,
                         id="Letters must be from ascii table"),
            pytest.param("Pass@word1", True,
                         id="Should return True as password is valid"),
            pytest.param("pass@word1", False,
                         id="Should have at least one upper letter"),
            pytest.param("Password1", False,
                         id="Should have at least one special character"),
            pytest.param("Pass@word", False,
                         id="Should have at least one digit"),
        ]
    )
    def test_check_password(self,
                            input_password: str,
                            expected_bool: bool) -> None:
        assert check_password(input_password) == expected_bool

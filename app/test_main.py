import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, result",
        [
            pytest.param(
                "Pass@word1",
                True,
                id="Should return True if password is 'Pass@word1'"
            ),
            pytest.param(
                "P@2swordpasswordp",
                False,
                id="Should return False if password is 'P@2swordpasswordp'"
            ),
            pytest.param(
                "h5$#!st5_2-0@s!&",
                False,
                id="Should return False if password is 'h5$#!st5_2-0@s!&'"
            ),
            pytest.param(
                "P@ss123",
                False,
                id="Should return False if password is 'P@ss123'"
            ),
            pytest.param(
                "H@ck me",
                False,
                id="Should return False if password is 'H@ck me'"
            ),
            pytest.param(
                "tRytoh@ckme",
                False,
                id="Should return False if password is 'tRytoh@ckme'"
            )
        ]
    )
    def test_password_check(
            self,
            password: str,
            result: bool
    ) -> None:
        assert check_password(password) == result

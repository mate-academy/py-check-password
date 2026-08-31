from app.main import check_password

import pytest


class TestCheckPassword:

    @pytest.mark.parametrize(
        "password,result",
        [
            ("P@ss1wd", False),
            ("Pass@word1passwor", False),
            ("Pass@word", False),
            ("Password1", False),
            ("pass#word2", False)
        ]
    )
    def test_check_password_is_correct(
            self, password: str,
            result: bool
    ) -> None:

        assert check_password(password) == result

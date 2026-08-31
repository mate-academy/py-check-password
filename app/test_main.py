import pytest

from app.main import check_password


class TestPasswordCheck:
    @pytest.mark.parametrize(
        "password,expected_result",
        [
            pytest.param(
                "Pass@word1",
                True,
                id="'Pass@word1' is a valid password"
            ),
            pytest.param(
                "qwerty",
                False,
                id="password should be at least 8 characters"
            ),
            pytest.param(
                "Str@ng",
                False,
                id="password should be at least 8 characters"
            ),
            pytest.param(
                "Passssswoooord11@!",
                False,
                id="password can not be bigger than 16 characters"
            ),
            pytest.param(
                "1P#",
                False,
                id="password should be at least 8 characters"
            ),
            pytest.param(
                "passw1ord!",
                False,
                id="password should have at least one upper case letter"
            ),
            pytest.param(
                "Pass2ord",
                False,
                id="password should have at least one special character"
            ),
            pytest.param(
                "Pass!ord",
                False,
                id="password should have at least one digit"
            )
        ]
    )
    def test_cat_and_dog_years(
            self,
            password: str,
            expected_result: bool
    ) -> None:
        assert check_password(password) == expected_result

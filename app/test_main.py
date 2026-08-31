import pytest

from app.main import check_password


class TestCheckPassword:

    @pytest.mark.parametrize(
        "password,expected_response",
        [
            pytest.param(
                "Pass@word",
                False,
                id="False if the password without digits"
            ),
            pytest.param(
                "Pass@word12345678",
                False,
                id="False if the password is longer than sixteen symbol"
            ),
            pytest.param(
                "Qwert1@",
                False,
                id="False if the password is shorter than eight symbol"
            ),
            pytest.param(
                "qwerty-123",
                False,
                id="False if the passwords without uppercase letter"
            ),
            pytest.param(
                "Trädgård_1",
                False,
                id="False if the letters are not of the Latin alphabet"
            ),
            pytest.param(
                "Password123",
                False,
                id="False if password without special character $@#&!-_"
            ),
            pytest.param(
                "Pass@word1",
                True,
                id=(
                    "True if the password is correct: 8-16 chars,"
                    "1 digit, 1 special char, 1 uppercase"
                )
            )

        ]
    )
    def test_check_password(
        self,
        password: str,
        expected_response: bool
    ) -> None:
        assert check_password(password) == expected_response

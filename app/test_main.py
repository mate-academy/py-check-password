from app.main import check_password

import pytest


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password,expected",
        [
            (
                "Pass@word1",
                True
            ),
            (
                "qwerty",
                False
            ),
            (
                "Str@ng",
                False
            ),
            (
                "PASSWORD1223@SDF",
                True
            ),
            (
                "6546@6fsdfdf",
                False
            ),
            (
                "Aslfjthgndjeufj@o123",
                False
            ),
            (
                "Str@ng1",
                False
            ),
            (
                "Afsdfsa@fsdd",
                False
            ),
            (
                "Academia123",
                False
            )
        ]
    )
    def test_correct_output(self, password: str, expected: bool) -> None:
        assert check_password(password) == expected

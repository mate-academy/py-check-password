import pytest

from app.main import check_password


class TestCheckPassword:

    @pytest.mark.parametrize(
        "password, expected_result",
        [
            ("Password1@", True),
            ("Passw!1", False),
            ("Password123%", False),
            ("ABCDab!@#", False),
            ("abcdefgh123!", False),
            ("Abcdefgh1234$!!!!", False),
            ("Password123", False),
        ],
        ids=[
            "Should return True",
            "Should be at least 8 characters",
            "Should be only this special character $@#&!-_",
            "Should contains 1 digit",
            "Should contains 1 uppercase letter",
            "Should be maximum 16 characters inclusive",
            "Should contains 1 special character"
        ]
    )
    def test_should_return_expected_result(
            self, password: str, expected_result: bool
    ) -> None:
        assert check_password(password) is expected_result

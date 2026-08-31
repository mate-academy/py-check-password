import pytest

from app.main import check_password


def test_check_password_should_return_boolean() -> None:
    assert isinstance(check_password(""), bool)


class TestCheckPasswordClass:
    @pytest.mark.parametrize(
        "password, expected_result",
        [
            pytest.param(
                "Pяssword1!",
                False,
                id="should return 'false' for password "
                   "with non-Latin character"
            ),
            pytest.param(
                "password1!",
                False,
                id="should return 'false' for password "
                   "without any uppercase char"
            ),
            pytest.param(
                "Password!",
                False,
                id="should return 'false' for password without any digit"
            ),
            pytest.param(
                "Password1",
                False,
                id="should return 'false' for password "
                   "without any special char"
            ),
            pytest.param(
                "Passw1!",
                False,
                id="should return 'false' for too weak password"
            ),
            pytest.param(
                "P@ssword123456789",
                False,
                id="should return 'false' for too long password"
            ),
            pytest.param(
                "P@ssword1",
                True,
                id="should return 'true' for the valid password "
                   "with 8 characters"
            ),
        ]
    )
    def test_check_password(
            self,
            password: str,
            expected_result: bool,
    ) -> None:
        assert check_password(password) == expected_result

import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="should return True if password is correct"
        ),
        pytest.param(
            "password",
            False,
            id="should return False if no uppercase, special char and digit"
        ),
        pytest.param(
            "Password",
            False,
            id="should return False if only uppercase"
        ),
        pytest.param(
            "password1@",
            False,
            id="should return False if no uppercase"
        ),
        pytest.param(
            "Password1",
            False,
            id="should return False if no special character"
        ),
        pytest.param(
            "Password@",
            False,
            id="should return False if no digit"
        ),
        pytest.param(
            "qWe2@2y",
            False,
            id="should return False if length is less than 8"
        ),
        pytest.param(
            "aWerty12345@3eafkjlkrfrwgsdfgaefdf",
            False,
            id="should return False if length is more than 16"
        )
    ]
)
def test_check_password(password: str,
                        expected_result: bool) -> None:
    assert check_password(password) == expected_result

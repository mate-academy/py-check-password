import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="should return `True`, "
               "because `Pass@word1` is valid password"
        ),
        pytest.param(
            "Qwerty!@#",
            False,
            id="should return `False`, "
               "because `qwerty` does not consist digits"
        ),
        pytest.param(
            "$Tr0ng",
            False,
            id="should return `False`, "
               "because `Str@ng` is too short password"
        ),
        pytest.param(
            "Password123!@#4561",
            False,
            id="should return `False` for too long password length"
        ),
        pytest.param(
            "password123!@#",
            False,
            id="should return `False`, "
               "because `password123!@#` does not consist uppercase letters"
        ),
        pytest.param(
            "Password123",
            False,
            id="should return `False`, "
               "because `Password123` does not consist spec symbols"
        )
    ]
)
def test_password_validation_func(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result

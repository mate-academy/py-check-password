import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_answer",
    [
        pytest.param(
            "Pass@w1",
            False,
            id="should check minimal password length"
        ),
        pytest.param(
            "@@@123456",
            False,
            id="should check if password have letters"
        ),
        pytest.param(
            "Pass%word1",
            False,
            id="should accept special character from $@#&!-_"
        ),
        pytest.param(
            "Pass@word1Pass@word1",
            False,
            id="should check maximum password length"
        ),
        pytest.param(
            "Pass@words",
            False,
            id="should contain at least 1 digit"
        ),
        pytest.param(
            "pass@word1",
            False,
            id="should contain at least 1 upper"
        ),
        pytest.param(
            "Passsword1",
            False,
            id="should contain at least 1 special symbol"
        )
    ]
)
def test_results_of_check_password(
        password: str,
        expected_answer: bool
) -> None:
    assert check_password(password) == expected_answer

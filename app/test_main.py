import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "input_password,is_the_password_correct",
    [
        pytest.param(
            "1@A456789",
            True,
            id="check range password and check for required characters"
        ),
        pytest.param(
            "123456789",
            False,
            id="only intenger in password"
        ),
        pytest.param(
            "jfhusJDfij",
            False,
            id="only letter in password"
        ),
        pytest.param(
            "@#_!!@#!-",
            False,
            id="only special characters in password"
        ),
        pytest.param(
            "12@#hfudh",
            False,
            id="password without uppercase letter"
        ),
        pytest.param(
            "3A#",
            False,
            id="short password"
        ),
        pytest.param(
            "1232313ADDSDH#$!@!@#!HAU123",
            False,
            id="too long password"
        ),
        pytest.param(
            "ADHU!@#ds",
            False,
            id="password without digits"
        )
    ]
)
def test_total_function(
    input_password: str,
    is_the_password_correct: bool
) -> None:
    result = check_password(input_password)
    assert result == is_the_password_correct

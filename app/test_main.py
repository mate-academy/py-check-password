import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "",
            False,
            id="Empty password"
        ),
        pytest.param(
            "@Jiaoijr",
            False,
            id="Password without digits, 8 characters long"
        ),
        pytest.param(
            "Jofi1234r",
            False,
            id="Password without special character longer than 8 characters"
        ),
        pytest.param(
            "81791723@!$",
            False,
            id="Password without letter, longer than 8 characters"
        ),
        pytest.param(
            "@jijoJ9",
            False,
            id="Password shorter than 8 characters"
        ),
        pytest.param(
            "@j9fjewn93fp93fuij8u!9Jadsfjpoewi",
            False,
            id="Password longer then 16 characters"
        ),
        pytest.param(
            "9jD83N!ty",
            True,
            id="Correct password"
        )
    ]
)
def test_different_passwords(password: str, result: bool) -> None:
    assert (
        check_password(password) == result
    ), f"Password: {password} should be {result}"

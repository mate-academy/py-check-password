from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,expected_output",
    [
        ("Blo8_", False),
        ("Macarena_@6rake!_Dan$e", False),
        ("Паруль_М0цик", False),
        ("P@$$w0rd", True)
    ],
    ids=[
        "check if len(password) < 8 is False",
        "check if len(password) > 16 is False",
        "check if non-latin password is False",
        "check for at least 1 digit, 1 special character, 1 uppercase letter",
    ]
)
def test_correct_password_validation(
        password: str,
        expected_output: bool
) -> None:
    assert check_password(password) == expected_output

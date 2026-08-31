import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_value",
    [
        ("M@te1Academy", True),
        ("M@te1", False),
        ("M@te1M@te1M@te1M@te1M@te1M@te1M@te1", False),
        ("Mate1Academy", False),
        ("M@teAcademy", False),
        ("m@te1academy", False),
        ("M|тe1Academy", False),
    ]
)
def test_check_password(password: str, expected_value: bool) -> None:
    assert check_password(password) == expected_value

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "test_password, check_result",
    [
        ("Йцукен1!_", False),
        ("Qw#_", False),
        ("Qwerty12#$5________________", False),
        ("12345678", False),
        ("!@#$!______", False),
        ("Password1#", True)
    ]
)
def test_checks_password_correctly(
        test_password: str,
        check_result: bool
) -> None:
    assert check_password(test_password) == check_result

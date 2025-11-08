import pytest
import app.main as main


@pytest.fixture
def sample_passwords() -> dict[str, str]:
    return {
        "valid": "Soloway$31",
        "too_short": "Ab1!",
        "too_long": "Abcdefghijklmnopqrstuvwx1!",
        "no_upper": "password1$",
        "no_digit": "Password$",
        "no_special": "Password1",
    }


def test_check_password_short(sample_passwords: dict[str, str]) -> None:
    assert main.check_password(sample_passwords["too_short"]) is False


def test_check_password_long(sample_passwords: dict[str, str]) -> None:
    assert main.check_password(sample_passwords["too_long"]) is False


def test_check_password_no_special(sample_passwords: dict[str, str]) -> None:
    assert main.check_password(sample_passwords["no_special"]) is False


def test_check_password_without_uppercase(
        sample_passwords: dict[str, str]
) -> None:
    assert main.check_password(sample_passwords["no_upper"]) is False


def test_check_password_without_digits(
        sample_passwords: dict[str, str]
) -> None:
    assert main.check_password(sample_passwords["no_digit"]) is False


def test_check_password_valid(sample_passwords: dict[str, str]) -> None:
    assert main.check_password(sample_passwords["valid"]) is True

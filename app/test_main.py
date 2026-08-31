import pytest

from app.main import check_password


@pytest.mark.parametrize("password", [
    "Pass@word1",
    "Passw$ords2",
    "Pass#w&rd1!",
    "Pass-w_rd1",
    "P@ssw0rd16chars-",
    "P@ssw0rd!",
])
def test_valid_passwords_should_return_true(password: str) -> None:
    assert check_password(password) is True


@pytest.mark.parametrize("password", [
    "a@bC1",
    "qwerty",
    "PasswordTooLong!123",
    "toolongpassword@123",
    "password@123",
    "Password@word",
    "Password123",
    "Password?123",
    "",
    "12345678",
])
def test_invalid_passwords_should_return_false(password: str) -> None:
    """Перевіряє, що невалідні паролі повертають False."""
    assert check_password(password) is False

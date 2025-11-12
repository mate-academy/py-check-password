import pytest
from app.main import check_password


@pytest.mark.parametrize("password", [
    "Pass@word1",
    "A1!bcdefghijklmn",
    "P1@ssworD",
    "Te$tP@ssw0rd123"
])
def test_valid_passwords_return_true(password: str) -> None:
    assert check_password(password) is True


@pytest.mark.parametrize("password", [
    "short1",
    "TooLongP@ssw0rd17",
    "TooLongP@ssw0rd12345"
])
def test_invalid_length_returns_false(password: str) -> None:
    assert check_password(password) is False


@pytest.mark.parametrize("password", [
    "p@ssw0rd",
    "p@ssword1",
    "12345678@",
    "smallp@ssw0rd"
])
def test_missing_uppercase_returns_false(password: str) -> None:
    if len(password) in range(8, 17):
        assert check_password(password) is False


@pytest.mark.parametrize("password", [
    "P@ssword",
    "Test!haslo",
    "AAAA@@@!!!",
    "LongP@ssword"
])
def test_missing_digit_returns_false(password: str) -> None:
    if len(password) in range(8, 17):
        assert check_password(password) is False


@pytest.mark.parametrize("password", [
    "Paszl0wice",
    "TestHaslo1",
    "BIGPASSWORD123",
    "HasloBezCyfr"
])
def test_missing_special_char_returns_false(password: str) -> None:
    if len(password) in range(8, 17):
        assert check_password(password) is False


@pytest.mark.parametrize("password", [
    "P@ss w0rd1",
    "Póss@word1",
    "P@ssw0rd%",
    "P@ssw0rd^",
    "P@ssw0rd{",
    "P@ssw0rd^"
])
def test_forbidden_characters_returns_false(password: str) -> None:
    assert check_password(password) is False


@pytest.mark.parametrize("password", [
    "qwerty",
    "Str@ng",
])
def test_example_negative_cases(password: str) -> None:
    assert check_password(password) is False

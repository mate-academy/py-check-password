import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False)
    ]
)
def test_provided_examples(password: str, expected: bool) -> None:
    assert check_password(password) is expected


@pytest.mark.parametrize(
    "password",
    [
        "Abcdef1!",
        "MyPass@2",
        "Strong#9",
        "Valid$password3",
        "Test_123A",
        "Secure-4U"
    ]
)
def test_valid_passwords_parametrized(password: str) -> None:
    assert check_password(password)


@pytest.mark.parametrize(
    "password",
    [
        "Pass@1",
        "A1!",
        "VeryLongPassword@123",
        "password@123",
        "Password@",
        "Password123",
        "Password@123%",
        "Password@123*"
    ]
)
def test_invalid_passwords_parametrized(password: str) -> None:
    assert not check_password(password)


@pytest.mark.parametrize("length", [1, 2, 3, 7])
def test_too_short_lengths(length: int) -> None:
    password = "A" * (length - 3) + "1@A" if length >= 3 else "A" * length
    assert not check_password(password)


@pytest.mark.parametrize("length", [17, 18, 20, 25])
def test_too_long_lengths(length: int) -> None:
    password = "A" * (length - 3) + "1@A"
    assert not check_password(password)


@pytest.mark.parametrize("special_char", ["$", "@", "#", "&", "!", "-", "_"])
def test_special_chars_parametrized(special_char: str) -> None:
    password = f"Pass{special_char}1AB"
    assert check_password(password)


@pytest.mark.parametrize(
    "invalid_char",
    ["%", "*", "+", "=", "?", "/", "\\", "|"]
)
def test_invalid_special_chars(invalid_char: str) -> None:
    password = f"Pass{invalid_char}1AB"
    assert not check_password(password)


@pytest.mark.parametrize("length", [8, 12, 16])
def test_boundary_valid_lengths(length: int) -> None:
    base = "A1@"
    fill_length = length - len(base) - 1
    password = base + "a" * fill_length + "b"
    assert len(password) == length
    assert check_password(password)

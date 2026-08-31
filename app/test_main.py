import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password",
    [
        "Pass@word1",
        "Str0ng#Pass",
        "A1!aaaaa",  # exactly 8 characters - lower boundary
        "A1!aaaaaaaaaaaaa",  # exactly 16 characters - upper boundary
        "Qwerty1$",
        "MyP@ssw0rd123",
        "Zzzzzzz9#",
        "Test_1234",
        "Valid-Pass1",
        "Ab1&cdefgh",
        "ALLUPPERCASE1@",  # no lowercase required by the rules
    ],
)
def test_check_password_valid(password: str) -> None:
    assert check_password(password) is True


@pytest.mark.parametrize(
    "password",
    [
        "qwerty",
        "Str@ng",
        "short1A",  # 7 characters - just below lower boundary
        "A1!aaaaaaaaaaaaaa",  # 17 characters - just above upper boundary
        "alllowercase1@",  # no uppercase letter
        "NoDigitsHere@@",  # no digit
        "NoSpecial1234",  # no special character
        "12345678",  # only digits, no uppercase/special
        "!!!!!!!!",  # only special characters
        "Password",  # no digit, no special character
        "Pass word1@",  # contains a space (invalid character)
        "Pässword1@",  # contains non-Latin letter
        "Password1@#extra*",  # invalid special character '*'
        "",  # empty string
        "A1@aaaa",  # 7 characters total
    ],
)
def test_check_password_invalid(password: str) -> None:
    assert check_password(password) is False


def test_check_password_missing_digit() -> None:
    assert check_password("Password@") is False


def test_check_password_missing_special_char() -> None:
    assert check_password("Password1") is False


def test_check_password_missing_uppercase() -> None:
    assert check_password("password1@") is False


@pytest.mark.parametrize("special_char", list("$@#&!-_"))
def test_check_password_each_allowed_special_char(special_char: str) -> None:
    password = f"Pass1{special_char}word"
    assert check_password(password) is True


@pytest.mark.parametrize("invalid_char", list("*()%^+=~`<>,.?/\\|[]{};:'\""))
def test_check_password_disallowed_special_chars(invalid_char: str) -> None:
    password = f"Pass1{invalid_char}word"
    assert check_password(password) is False


def test_check_password_length_exactly_eight() -> None:
    assert check_password("Aa1!aaaa") is True


def test_check_password_length_exactly_sixteen() -> None:
    assert check_password("Aa1!aaaaaaaaaaaa") is True


def test_check_password_length_seven_too_short() -> None:
    assert check_password("Aa1!aaa") is False


def test_check_password_length_seventeen_too_long() -> None:
    assert check_password("Aa1!aaaaaaaaaaaaa") is False

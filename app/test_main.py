import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password",
    [
        "Pass@word1",
        "Abcdef1@",
        "Qwerty9#",
        "Valid-1A",
        "Strong_2B",
        "GoodPass3!",
        "A1@bcdefghijklm",
        "PASSWORD1@",
        "@@@@@@@A1",
    ],
)
def test_check_password_valid(password: str) -> None:
    assert check_password(password) is True


@pytest.mark.parametrize(
    "password",
    [
        "Str@ng",
        "A1@bcdefghijklmnop",
        "password@",
        "Password@",
        "password1@",
        "Password1",
        "Pass word1@",
        "Pass.word1@",
        "Pass*word1",
        "Пароль1@",
        "Passwörd1@",
        "12345678@",
    ],
)
def test_check_password_invalid(password: str) -> None:
    assert check_password(password) is False


@pytest.mark.parametrize(
    ("password", "expected"),
    [
        ("A1@bcdef", True),
        ("A1@bcde", False),
        ("A1@bcdefghijklm", True),
        ("A1@bcdefghijklmN", True),
        ("A1@bcdefghijklmNo", False),
    ],
)
def test_check_password_length_boundaries(
        password: str,
        expected: bool
) -> None:
    assert check_password(password) is expected

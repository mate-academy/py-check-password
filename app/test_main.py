import pytest
from app.main import check_password


@pytest.mark.parametrize("password", [
    "Pass@word1",
    "Strong1$A",
    "A1@aaaaa",
    "Test123#Ab",
    "Valid!Pwd9",
    "short1@A",
    "Test1234$",
])
def test_valid_passwords(password: str) -> None:
    assert check_password(password) is True


@pytest.mark.parametrize("password", [
    "thisisaverylong1@A",
    "12345678",
    "abcdefgh",
    "ABCDEFGH",
    "abcdEFGH",
    "abcd1234",
    "ABCD1234",
    "abcdEF12",
    "Abcdefg!",
    "1234!@#$",
    "Tęst1234@",
])
def test_invalid_passwords(password: str) -> None:
    assert check_password(password) is False


def test_boundary_lengths() -> None:
    assert check_password("A1@aaaaa") is True       # 8
    assert check_password("A1@aaaaaaaaaaaa") is True  # 16
    assert check_password("A1@aaaaaaaaaaaaaa") is False  # 17

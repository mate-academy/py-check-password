from app.main import check_password

import pytest


# Valid passwords that meet all requirements
@pytest.mark.parametrize(
    "password",
    [
        "Pass@word1",
        "ABCabc123@",
    ],
)
def test_valid_passwords(password: str) -> None:
    assert check_password(password) is True


@pytest.mark.parametrize(
    "password",
    [
        "Password1%",
        "A1*aaaaaa",
        "Pass word1@",
    ],
    ids=["%-char-invalid", "*-char-invalid", "space-invalid"],
)
def test_invalid_characters(password: str) -> None:
    assert check_password(password) is False


@pytest.mark.parametrize(
    "password",
    [
        "Pass@word",
        "Passw0rd1",
        "password@1",
    ],
    ids=[
        "missing-digit",
        "missing-special-char",
        "missing-uppercase",
    ],
)
def test_missing_requirements(password: str) -> None:
    assert check_password(password) is False


@pytest.mark.parametrize(
    "password,expected",
    [
        ("A1@aaaaa", True),
        ("A1@aaaaaaaaaaaaa", True),
        ("A1@aaa", False),
        ("A1@aaaaaaaaaaaaaa", False),
    ],
    ids=[
        "8-chars-valid",
        "16-chars-valid",
        "7-chars-invalid",
        "17-chars-invalid",
    ],
)
def test_boundary_lengths(password: str, expected: bool) -> None:
    assert check_password(password) is expected

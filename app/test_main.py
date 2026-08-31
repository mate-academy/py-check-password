import pytest
from app.main import check_password


@pytest.mark.parametrize("password", [
    "Pass@wordaa1",
    "A1!bcdef",
    "Abcdef1!Ghijlm",
    "Aa!1bcdef"
])
def test_valid_password(password: str) -> None:
    assert check_password(password) is True


@pytest.mark.parametrize("password", [
    "A1!bc",
    "A1!" + "b" * 20,
    "a!1bcdefgh",
    "a!abdefgh",
    "A1bcdefgh",
    "A1!бсдефг",
    "A*1bcdefgh",
])
def test_invalid_password(password: str) -> None:
    assert check_password(password) is False

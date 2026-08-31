import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param("Pass@word1", True, id="Test when password is OK"),
        pytest.param(
            "Pass@w1", False,
            id="Test when password is too short"),
        pytest.param(
            "Pass@word1Pass@word1", False,
            id="Test when password is too long"),
        pytest.param(
            "qwertyqwerty", False,
            id="Test when password is without digits, specials and uppercase"),
        pytest.param(
            "Pass@word", False,
            id="Test when password is without digits"),
        pytest.param(
            "Password1", False,
            id="Test when password is without specials"),
        pytest.param(
            "pass@word1", False,
            id="Test when password is without uppercase"),
        pytest.param(
            "ЇPass@word1", False,
            id="Test when password has non Latin alphabet"),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

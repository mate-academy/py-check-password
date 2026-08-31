import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param("Ab$1", False, id="too short password"),
        pytest.param("Ab$1" * 5, False, id="too long password"),
        pytest.param("abcdefgh", False, id="only lowercase password"),
        pytest.param("ABCDEFGH", False, id="only uppercase password"),
        pytest.param("12345678", False, id="only digits password"),
        pytest.param("_" * 8, False, id="only special chars password"),
        pytest.param("abcdEFG$", False, id="no digits in password"),
        pytest.param("abcdEFG1", False, id="no special symbols in password"),
        pytest.param("abcd123$", False, id="no uppercase letter in password"),
        pytest.param(
            "a_B1cD3^f", False, id="password with incorrect special char"
        ),
        pytest.param("a_B1cD3$f", True, id="correct password"),
    ],
)
def test_returns_correct_results(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

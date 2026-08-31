import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param("Pass@word1", True, id="correct password"),
        pytest.param("Qw@rt1", False, id="len < 8"),
        pytest.param("qwertyuio@1", False, id="without uppercase letter"),
        pytest.param("Q1wertyuiop", False, id="without special character"),
        pytest.param("Pass@word", False, id="without digits"),
        pytest.param("Pass@word1234567890", False, id="len > 16"),

    ],
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

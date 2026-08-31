import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "test_input, bool_expected",
    [
        pytest.param("Pass@word1", True),
        pytest.param("Passwo1@", True),
        pytest.param("№222asswo1@", False),
        pytest.param("password1@", False),
        pytest.param("Passwo1@Passwo1@", True),
        pytest.param("\u2116asswo1@", False),
        pytest.param("Pa1ss@", False),
        pytest.param("d", False),
        pytest.param("", False),
        pytest.param("KJHJkbcsjdbcsdhb#8d7sd87csdsdfdsf@", False),
        pytest.param("jsndvinvfffG22", False),
        pytest.param("HHjjjj@@##", False),
    ]
)
def test_check_password(test_input: str, bool_expected: bool) -> None:
    assert check_password(test_input) == bool_expected

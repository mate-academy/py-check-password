import pytest
import app.main as main


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param("Pass@word1", True),
        pytest.param("Pa@1", False),
        pytest.param("Pass@word123456789", False),
        pytest.param("pass@word1", False),
        pytest.param("Pass@word", False),
        pytest.param("Password1", False),
        pytest.param("Pass%word1", False),
    ]
)
def test_check_password(value: str, expected: bool) -> None:
    assert main.check_password(value) == expected

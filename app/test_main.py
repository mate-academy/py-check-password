import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "initial_value,expected_result",
    [
        pytest.param("1Qwerty@", True, id="len min - True"),
        pytest.param("1Qwertyuiopasdf@", True, id="len max - True"),
        pytest.param("1Qwert@", False, id="len min - False"),
        pytest.param("1Qwertyuiopasdfg@", False, id="len max - False"),
        pytest.param("1qwerty@", False, id="hes no upper"),
        pytest.param("aQwerty@", False, id="hes no number"),
        pytest.param("1Qwerty", False, id="hes no special")
    ]
)
def test_check_password(
        initial_value: str,
        expected_result: bool
) -> None:
    assert check_password(initial_value) == expected_result

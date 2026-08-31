import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "input_value,expected_result",
    [
        ("Pass@word1", True),
        ("Password1", False),
        ("str0ng@st", False),
        ("Pass@word", False),
        ("P@ss1", False),
        ("Pass@word1Pass@word1Pass@word1", False),
    ]
)
def test_check_password(input_value: str, expected_result: bool) -> None:
    assert check_password(input_value) == expected_result

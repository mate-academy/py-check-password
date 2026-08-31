import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, boolean_value",
    [
        ("Pass@word1", True),
        ("Pass@word", False),
        ("Pass@word1wertyuq", False),
        ("Password1w", False),
        ("P@word1", False),
        ("pass@word1", False),
    ]
)
def test_should_output_correct_boolean_value(
    password: str,
    boolean_value: bool
) -> None:
    assert check_password(password) == boolean_value

from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "testing_value, expected_value",
    [
        ("Pass@word1", True),
        ("Pas@wrdы1", False),
        ("Password1", False),
        ("Pass@word", False),
        ("pass@word1", False),
        ("qwerty", False),
        ("Pas@word1password", False)
    ],
)
def test_check_password(testing_value: str, expected_value: bool) -> None:
    assert check_password(testing_value) == expected_value

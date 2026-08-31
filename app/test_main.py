import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "testing_value, expected_value",
    [
        ("Pass@word1", True),
        ("Pas@wёrd1", False),
        ("Password1", False),
        ("Pass@word", False),
        ("pass@word1", False),
        ("Pas@wo1", False),
        ("Pas@word1password", False)
    ],
)
def test_check_password(testing_value: str, expected_value: bool) -> None:
    assert check_password(testing_value) == expected_value

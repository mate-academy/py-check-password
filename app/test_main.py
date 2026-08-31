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
    ids=[
        "Correct example",
        "Should contain only letters of the Latin alphabet Aa-Zz",
        "Does`nt contain at least 1 special character from $@#&!-_",
        "Does`nt contain at least 1 digit",
        "Does`nt contain at least 1 uppercase letter",
        "Less than 8 characters",
        "More than 16 characters"
    ]
)
def test_check_password(testing_value: str, expected_value: bool) -> None:
    assert check_password(testing_value) == expected_value

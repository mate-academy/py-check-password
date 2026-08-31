import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("pass@word1", False),
        ("Password1", False),
        ("qwerty", False),
        ("Str@ng", False),
        ("P@ssw0rd", True),
        ("12345678", False),
        ("Short@1", False),
        ("Pass@word1Pass@word1", False),
        ("ValidP@ssw0rd", True),
        ("Special#P@ss", False),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_bool",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("P@w1", False),
        ("pass@word1", False),
        ("Pass@word", False),
        ("Pppaaasssass@word1", False),
        ("Password1", False)
    ]
)
def test_check_password(password: str, expected_bool: bool) -> None:
    assert check_password(password) == expected_bool

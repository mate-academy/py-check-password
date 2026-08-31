import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("", False),
        ("Ab_3", False),
        ("QWERty$@#&!-123456", False),
        ("qwerty5_", False),
        ("QWer_y!lay", False),
        ("STrii1ng", False),
        ("Pass@word1", True)
    ],
    ids=[
        "invalid if empty string",
        "invalid if less than 8 characters",
        "invalid if more than 16 characters",
        "invalid accept if no capitals",
        "invalid accept if no digits",
        "invalid accept without special sign from $@#&!-_",
        "valid if meets all criteria"
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

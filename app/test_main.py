import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Destination2", False),
        ("Sta1rway_to_Heaven", False),
        ("voule7-vous", False),
        ("Something!", False),
        ("P1ace_", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("pass@word1", False),
        ("Q1@ey", False),
        ("Str@ng", False),
        ("A@asddssds", False),
        ("Qert1212334", False),
        ("Qerteds23djnbf@jjciu", False),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

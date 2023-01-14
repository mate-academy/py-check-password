import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,response",
    [
        ("Str@ng1", False),
        ("only1owerc@se", False),
        ("Extreme11yLongP@sword", False),
        ("Forbidden%^)", False),
        ("WithoutDigit", False),
        ("W1thoutSpecChar", False),
        ("Pass@word1", True)
    ]
)
def test_cases_of_password(password: str, response: bool) -> None:
    assert (check_password(password) == response)

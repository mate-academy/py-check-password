import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Short3#", False),
        ("Length_8", True),
        ("MaximumLength_16", True),
        ("Very_long_password12", False),
        ("Пароль_35", False),
        ("No_digits", False),
        ("no_upper5", False),
        ("N0special", False),
        ("", False),
        ("Good_password1", True),
    ]
)
def test_can_access_google_page_accessible(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result

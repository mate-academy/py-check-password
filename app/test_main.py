import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, results",
    [
        ("Valid1@", False),
        ("ValidPassword123@", False),
        ("short1@", False),
        ("VeryLongPassword123@", False),
        ("12345678", False),
        ("password@", False),
        ("password1", False),
        ("1@Short", False),
        ("Valid@123", True),
        ("NoSpecialChar1", False),
        ("NoUppercase1@", True),
        ("Valid1#password", True),
        ("lowercase1@", False),
        ("uppercase@1", False),
        ("1234@abcD", True),
        ("wamdomawodma", False),
        (" ", False),
        ("Wawddawd@", False)
    ]
)
def test_check_password(
    password: str,
    results: bool
) -> None:
    assert check_password(password) == results

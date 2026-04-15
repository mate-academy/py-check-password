import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Pass123!", True,
            id="Valid password 8 chars"
        ),
        pytest.param(
            "VeryLongPass99#&", True,
            id="Valid password 16 chars"
        ),
        pytest.param(
            "A1#bcdefgh", True,
            id="Valid with mixed types"
        ),

        pytest.param(
            "Short1!", False,
            id="Too short (7 chars)"),
        pytest.param(
            "VeryLongPassword123!", False,
            id="Too long (20 chars)"
        ),

        pytest.param(
            "password123!", False,
            id="Missing uppercase"
        ),
        pytest.param(
            "Pass!!!!!", False,
            id="Missing digits"
        ),
        pytest.param(
            "Password123", False,
            id="Missing special characters"
        ),

        pytest.param(
            "Pass123! ", False,
            id="Contains space"
        ),
        pytest.param(
            "Pass123!%", False,
            id="Contains invalid special char (%)"
        ),
        pytest.param(
            "Пароль123!", False,
            id="Contains cyrillic letters"
        ),
        pytest.param(
            "Pass123!😊", False,
            id="Contains emoji"
        ),

        pytest.param(
            "P1#abcde", True,
            id="Boundary: exactly 8 chars"),
        pytest.param(
            "P1#abcdefghijkl", True,
            id="Boundary: exactly 16 chars"
        ),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password_variant, result",
    [
        pytest.param("Pass@word11111111", False, id="Too long password"),
        pytest.param("P@word1", False, id="Too short password"),
        pytest.param("qwerty#123", False, id="No uppercase letter"),
        pytest.param("Qwerty@pass", False, id="No digits"),
        pytest.param("Qwerty1pass", False, id="No special character"),
        pytest.param("Pass@word1", True, id="Valid password")
    ]
)
def test_check_password(password_variant: str, result: bool) -> None:
    assert check_password(password_variant) == result

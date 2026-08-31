import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("hnkjuinlmij", False),
        ("kN8@", False),
        ("jnmlj7@o", False),
        ("Pass@word1hnkjuinlmij", False),
        ("Hnkjuinlmij@", False)
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result

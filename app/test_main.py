from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,is_correct",
    [
        ("Pass@word1", True),
        ("qwert@!y1", False),
        ("qw@wda1wddddaQdwaawdawawdawdty", False),
        ("qwertyQ@@!", False),
        ("qwertyawdQ1", False),
        ("Str@n1", False),
    ]
)
def test_should_return_correct_value(
        password: str,
        is_correct: bool
) -> None:
    assert check_password(password) == is_correct

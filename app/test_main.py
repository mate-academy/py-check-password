import pytest

from app.main import check_password

test_data = [
    ("Pass@wo1", True),
    ("Pass@w1", False),
    ("1@qwerty", False),
    ("Str@ngaq", False),
    ("1Strangx", False),
    ("Pass@wor1qwertyS", True),
    ("Pass@wor1qwertySa", False),
    ("Pasś@wo1", False),
    ("Pas s@w1", False),
]


@pytest.mark.parametrize("password, expected", test_data)
def test_password_has_correct_logic(
        password: str,
        expected: bool
) -> None:
    result = check_password(password)
    assert result is expected

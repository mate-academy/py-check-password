import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected",
                         [
                             ("Pass@word1", True),
                             ("qwerty", False),
                             ("Str@ng", False),
                             ("pa1@word", False),
                             ("Pa@words", False),
                             ("Pa1words", False),
                             ("Pa1@wordPa1@words", False),
                             ("Pa1@wor", False),
                             ("Pa1@word", True),
                             ("Pa1@wordPa1@word", True),
                         ])
def test_check_password_with_different_passwords(
    password: str,
    expected: bool,
) -> None:
    check_password(password)
    assert expected == check_password(password)

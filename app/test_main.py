import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_correct",
    [
        ("Pass@word1", True),
        ("Qwerty123", False),
        ("123", False),
        ("Qwert123#", True),
        ("Str@ng", False),
        ("Veryverylongpassowrd1$", False),
        ("Qwertyhgy#", False),
        ("123!Q", False),
        ("qwerty123$", False),
    ]
)
def test_check_password(password: str, is_correct: bool) -> bool:
    assert check_password(password) == is_correct

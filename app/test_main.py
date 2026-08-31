import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("justlower4case", False),
        ("$mAl4", False),
        ("vEryLongPasswOrd444matEbig$", False),
        ("pythonTop1", False),
        ("Academy@&", False),
        ("england&789", False)
    ]
)
def test_should_return_correct_answer(password: str, result: bool) -> None:
    assert check_password(password) == result

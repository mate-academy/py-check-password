import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty@1", False),
        ("Qqwerty@", False),
        ("Qqwerty1", False),
        ("Str@ng", False),
        ("Qwerty123@qwerty123", False),
        ("Qw3@3", False)
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result

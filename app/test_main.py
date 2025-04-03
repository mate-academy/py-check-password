import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("!0A$@#&!-_", True),
        ("!0A$@#&!-_%", False),

        ("!0A123456789", True),
        ("!0Aabcdefghijklm", True),
        ("!0Anopqrstuvwxyz", True),
        ("!0ABCDEFGHIJKLMN", True),
        ("!0OPQRSTUVWXYZ", True),
        ("!0A45678Ą", False),

        ("!0A", False),
        ("!0Aaaaaaaaaaaaaaa", False),
        ("", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected


def test_check_password_exception() -> None:
    with pytest.raises(TypeError):
        check_password(None)

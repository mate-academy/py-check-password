from __future__ import annotations
import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, is_correct",
    [
        ("P@55wordQ#", True),
        ("", False),
        ("P@5wor", False),
        ("P@55wordP@ssw0rd1234", False),
        ("p@55wordq#", False),
        ("PA55WORD!!", True),
        ("PA$$word!!", False),
        ("PA55word77", False),
        ("PASSWORDXX", False),
        ("passwordxx", False),
        ("1234567890", False),
        ("$@#&!-_$@#&!-_", False),
        ("pĄssWORD!!", False),
    ],
    ids=[
        "Password is correct",
        "Password is empty",
        "Password is to short",
        "Password is to long",
        "Password has no upper letter",
        "Password has no lower letter",
        "Password has no digit",
        "Password has no special character",
        "Password has only upper letters",
        "Password has only lower letters",
        "Password has only digits",
        "Password has only special characters",
        "Password has non ascii letter"
    ]
)
def test(password: str, is_correct: bool) -> None:
    assert check_password(password) == is_correct

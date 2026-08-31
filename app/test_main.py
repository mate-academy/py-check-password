import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("D5b$gB", False),
        ("uxm9w4jT6!-d71T0go", False),
        ("gl4_bf5v9_x137", False),
        ("tFVjNt@qkHtFvfS", False),
        ("BRrKu5mgFddC", False),
        ("F2O$ucAHDe!-3", True)

    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) is result

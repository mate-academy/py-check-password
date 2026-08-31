import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "input_password, bool_result",
    [
        ("D5b$gB", False),
        ("uxm9w4jT6!-d71T0go", False),
        ("gl4_bf5v9_x137", False),
        ("tFVjNt@qkHtFvfS", False),
        ("BRrKu5mgFddC", False),
        ("F2O$ucAHDe!-3", True)
    ],
    ids=[
        "False for short passwords",
        "False for passwords longer than 17 symbols",
        "False for passwords without uppercase letter",
        "False for passwords without digits",
        "False for passwords without special symbols",
        "True for passwords from 8 to 17 symbols,"
        " with uppercase, digits and special symbols"
    ]
)
def test_check_password(
        input_password: str, bool_result: bool
) -> None:
    assert check_password(input_password) == bool_result

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    ("pass_to_check", "expected"),
    [
        ("hEll0_world!", True),
        ("hEll0world", False),
        ("hEllo_world!", False),
        ("hell0_world!", False),
        ("hEll0_w", False),
        ("hEll0_world!hEll0_world!", False),
        ("hEll0_worД", False),
        ("$@#&!-_@!!", False),
        ("38795980345", False),
        ("JVKALEIKLJDAA", False),
    ],
    ids=[
        "if valid password is provided",
        "if special characters are not provided",
        "if digits are not provided",
        "if uppercase characters are not provided",
        "if password too short",
        "if password too long",
        "if password contains invalid character",
        "if password contains only special characters",
        "if password contains only digits",
        "if password contains only uppercase chars",
    ]
)
def test_should_return_correct_value(
    pass_to_check: str,
    expected: bool
) -> None:
    assert check_password(pass_to_check) == expected

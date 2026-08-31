from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty@1ass", False),
        ("Str@ng1", False),
        ("Pass@wordd", False),
        ("Pass1wordd", False),
        ("Pass@word1ssssssssss", False),
    ],
)
def test_check_password(
        password: str,
        expected: bool
) -> None:
    assert check_password(password) == expected

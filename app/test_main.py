import pytest

from .main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Mate1_", False),
        ("Maaaaaaaateeeee111122222____", False),
        ("Mateacademy1_", True),
        ("mateacademy1_", False),
        ("Mateacademy1_", True),
        ("Mateacademy1", False),
        ("Mateacademy1_", True),
        ("Mateacademy_", False),
    ]
)
def test_password_has_all_requirements(
        password: str,
        expected: bool
) -> None:
    assert check_password(password) == expected

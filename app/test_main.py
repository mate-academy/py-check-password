from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        ('Pass@word1', True),
        ('qwerty1#', False),
        ('Str@n9', False),
        ("S@bagfgdf", False),
        ("454364J@mesWakidzasi", False),
        ("Maks123445", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

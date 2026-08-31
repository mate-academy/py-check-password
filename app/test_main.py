import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("A1@bcdef", True),
        ("A1@bcde", False),
        ("A1@bcdefgwymnlshj", False),
        ("A@bcdefg", False),
        ("A1bcdefgw", False),
        ("a1@bcdefg", False),
        ("A1@bcdвfg", False),
        ("A1@bcdef", True),
        ("A1@bcdefgwymnlsh", True),
    ]
)
def test_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

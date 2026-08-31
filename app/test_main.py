import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("ABCDEFGHIJKLMN1$", True),
        ("OPQRSTUVWXYZ2@", True),
        ("OPQRSTUVWXYZ3#", True),
        ("OPQRSTUVWXYZ4&", True),
        ("OPQRSTUVWXYZ5!", True),
        ("OPQRSTUVWXYZ6-", True),
        ("7890OPQRSTUVWXY-", True),
        ("7890opqrstuvwxy-", False),
        ("opqrStuvwxy-", False),
        ("7890opqrstuvwxY", False),
        ("VWXYZ4&", False),
        ("ABCDEFGHIJKLMN1$3", False),
    ]
)
def test_check_password(password: str,
                        expected: bool
                        ) -> None:
    assert check_password(password) == expected

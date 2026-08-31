from app.main import check_password

import pytest


@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("P@s1", False),
        ("p@ssword1", False),
        ("P@ssword", False),
        ("Password1", False),
        ("P@ssword1P@ssword2P@ssword3", False),
        ("P@ssword1", True)
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

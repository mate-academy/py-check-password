import pytest

from app.main import check_password


@pytest.mark.parametrize("password_to_check, expected_result", [
    ("1Ab$cdef", True),
    ("Эфывй", False),
    ("Abcd1$", False),
    ("Ab1$qwertyuiopasdfghjkl", False),
    ("1ab$cdef", False),
    ("aAb$cdef", False),
    ("1Abccdef", False),
])
def test_check_password(password_to_check: str, expected_result: bool) -> None:
    assert check_password(password_to_check) == expected_result

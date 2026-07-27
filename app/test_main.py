from app.main import check_password
import pytest


@pytest.mark.parametrize("password,expected_result", [
    ("qWer@y1", False),
    ("Qwerty@1", True),
    ("Qwer$yuiopasdfg1", True),
    ("Qwe@1sdfawedfgrtg", False),
    ("qwert@u1", False),
    ("Qwert&u1", True),
    ("Qwert#u2", True),
    ("Qwert@uq", False),
    ("Qwert!u5", True),
    ("Qwertau3", False),
    ("Qwert-u7", True),
    ("Qweйt@u8", False),
])
def test_check_password_symbols(password: str, expected_result: bool) -> None:
    result = check_password(password)
    assert result == expected_result

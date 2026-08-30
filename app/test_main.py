import pytest

from app.main import check_password


@pytest.mark.parametrize("password,returned_value", [
    ("SleeP_PassworD1", True),
    ("SleeP1_", False),
    ("SleeP_PassworD", False),
    ("SleeP_PassworD111", False),
    ("sleep_password1", False),
    ("SleePPassworD1", False),
    ("11111_1111111", False),
])
def test_passwords(password, returned_value):
    assert check_password(password) == returned_value

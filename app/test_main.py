from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Valid1@Ab", True),
        ("short1@", False),
        ("NoDigit@A", False),
        ("nodollar1A", False),
        ("Invalid space1@", False),
        ("A2345678@", True),
        ("qwerty123-", False),
        ("Titan_q1", True),
        ("Qwertyuiopasdf1!", True),
        ("Petyakley=1", False),
        ("Ab1!", False),
        ("Asdfghjklzxcvbnm_12!", False),
        ("Zxcvbnm1", False)
    ]
)
def test_check_password(password, expected):
    assert check_password(password) is expected

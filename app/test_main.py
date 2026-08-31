import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "user_password,expected",
    [
        ("aAabBb123", False), ("Pass@word1", True), ("qwerty", False),
        ("12345", False), ("Str@ng2", False), ("M8_Academy", True),
        ("AB123_veryLongPassword", False), ("psw0rd_w_o_upper", False),
        ("No_numbers", False)
    ]
)
def test_check_password(user_password: str, expected: bool) -> None:
    assert check_password(user_password) == expected

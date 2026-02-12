import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng1", False),
        ("sdfpjasdfjlxkljboijawer", False),
        ("asdrfvcxzbnh", False),
    ]
)
def test_check_password(password, expected_result):
    assert check_password(password) == expected_result

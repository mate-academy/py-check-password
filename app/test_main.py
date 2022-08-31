import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param("-Test12", False, id="too short"),
        pytest.param("@Password1234567890", False, id="too long"),
        pytest.param("#test123", False, id="without uppercase letter"),
        pytest.param("!!!!Test", False, id="without digits"),
        pytest.param("Test1234", False, id="without special symbols"),
    ]
)
def test_check_password(password, expected):
    assert check_password(password) == expected

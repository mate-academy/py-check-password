import pytest
from app.main import check_password
from unittest.mock import patch


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Abcdefg1$Abcdefg1$", False),
        ("Abcdefg1$Abcdefg", True),
        ("password@1", False),
        ("Abcdefg1$Ї", False)
    ]
)
def test_check_password(password: str,
                        expected: str) -> None:
    with patch("app.main.check_password") as mocked_password:
        mocked_password.return_value = expected
        assert check_password(password) == expected

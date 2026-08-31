import pytest

from unittest.mock import patch, Mock

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty1", False),
        ("Str@ng", False),
        ("Strong@pass1", True),
        ("str0ng@pass", False),
        ("TooLongPasswordW@thMoreThan16s", False),
        ("Str#ng@pass", False),
        ("S@2d", False)
    ]
)
@patch("app.main.check_password")
def test_check_password(
        mock_password: Mock,
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) is expected_result

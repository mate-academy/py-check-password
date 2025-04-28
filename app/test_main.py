import pytest

from unittest import mock

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Str@ng2", False),
        ("Pass@word1qwerty2", False),
        ("pass@word1", False),
        ("Pass@word", False),
        ("Password1", False)
    ],
    ids=[
        "password_ok",
        "less_than_8_characters",
        "more_than_16_characters_inclusive",
        "password_without_capital letter",
        "password_without_digit",
        "password_without_special_character"
    ]
)
@mock.patch("app.main.check_password")
def test_check_password(
        mock_check_password: mock.Mock,
        password: str,
        result: bool
) -> None:
    mock_check_password.return_value = password
    assert check_password(password) == result

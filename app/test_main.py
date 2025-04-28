import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("saSda@dsa", False),
        ("sdsadS4@ddsadadjhh", False),
        ("dasgdsS2", False),
        ("dsad$4dfs", False),
        ("Des@3", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("pass@word1", False),
        ("Password1", False),
        ("Pass@word", False),
        ("Pa@1", False),
        ("qwerty", False),
        ("Str@ng", False),
        ("Str@ngsdegdergsef#EDQ1wd", False),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

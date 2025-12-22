import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pass@word", False),
        ("Password1", False),
        ("pass@word1", False),
        ("Ab1$eAb1$eAb1$eAb1$eAb1$eAb1$eAb1$e", False),
        ("Ab1$e", False)
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

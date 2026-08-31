import pytest as pytest

from app.main import check_password


@pytest.mark.parametrize(
    "check_in_password, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pas@1", False),
        ("Password@12345678", False),
        ("Password1@u", True),
        ("passworfd1!", False),
        ("Password!#", False),
        ("Password1", False)

    ]
)
def test_check_password(check_in_password: str, expected_result: bool) -> None:
    assert check_password(check_in_password) == expected_result

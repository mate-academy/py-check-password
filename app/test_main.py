import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "pass_to_check, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("PassPass@word1234", False),
        ("апжВ!pass", False),
        (" ", False),
        ("12!A", False),
        ("Password1", False),
        ("password1!", False)
    ]
)
def test_should_check_pass(pass_to_check: str, expected_result: bool) -> None:
    assert check_password(pass_to_check) == expected_result

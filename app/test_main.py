import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "test_password,expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pass@word", False),
        ("Pass@word123456789", False),
        ("Password", False),
        ("P@sswo1", False),
        ("Password1", False),
        ("pass@word1", False)
    ]
)
def test_check_password(
        test_password: str,
        expected_result: bool
) -> None:
    assert check_password(test_password) == expected_result

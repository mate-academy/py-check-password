import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("P@ss1", False),
        ("A" * 21, False),
        ("password1@", False),
        ("Password@", False),
        ("Password1", False),
        ("", False),
        ("gfijsB@d5sffdfsdfsdf", False)
    ],
)
def test_check_password(password: str, expected_result: bool) -> None:
    result = check_password(password)
    assert result == expected_result

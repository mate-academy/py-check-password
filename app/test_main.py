import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, except_result",
    [
        ("Pass@word1", True),
        ("qwerty1234", False),
        ("S@ng1", False),
        ("Strng@1234567890asdfasdf", False),
        ("Pass@word", False),
        ("password1", False),
        ("Password1", False),
        ("pass@word1", False),
    ]
)
def test_check_password(password: str, except_result: bool) -> None:
    result = check_password(password)
    assert result == except_result

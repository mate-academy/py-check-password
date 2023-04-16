import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "string,result",
    [
        ("Pass@word1", True),
        ("P@ert1", False),
        ("pass@word1", False),
        ("Pass@word1Pass@word1", False),
        ("Password1", False),
        ("Pass@word", False)
    ]
)
def test_check_password_is_valid(string: str, result: bool) -> None:
    assert check_password(string) == result

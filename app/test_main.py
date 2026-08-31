import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("pass@word1", False),
        ("Pass@wordI", False),
        ("D3b@t", False),
        ("Pass@word1Pass@word1", False),
        ("Passqword1", False)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

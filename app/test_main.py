import pytest

from .main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("Q1#rty", False),
        ("Str@ng", False),
        ("1WE@dfghgfsfdsfherjhgdgnfg", False),
        ("A@@@@@@@@@@", False),
        ("1aAAAAAAAAAAA", False),
        ("sdffdf334@", False)
    ]

)
def test_check(
        password: str, result: bool
) -> None:
    assert check_password(password) == result

import pytest
from app.main import check_password


def test_should_return_bool() -> None:
    assert (
        isinstance(check_password("look"), bool) is True
    ), "Function 'check_password' should return bool"


@pytest.mark.parametrize(
    "password, bool_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Тsіwo@@rd", False),
        ("Pass@word1Pass@word1Pass@word1", False),
        ("012345678", False),
        ("", False),
        ("Pass@word", False),
        ("Password11", False),
        ("pass@@word11", False),
        ("Pa@wor1", False),
    ]
)
def test_check_password(password: str, bool_result: bool) -> None:
    assert check_password(password) == bool_result

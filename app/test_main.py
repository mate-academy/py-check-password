import pytest
from .main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("passqweword", False),
        ("Qwert1!", False),
        ("Str@ng", False),
        ("Pass@word1Pass@word1", False),
        ("", False),
        ("Pass@!word2", True),
    ]
)
def test_should_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) is result

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("P@d1", False),
        ("Pass@word11234567", False),
        ("pass@word1", False),
        ("Password1", False),
        ("Pass@word", False)
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result

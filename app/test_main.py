import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Shor@e1", False),
        ("кириллица", False),
        ("Thisp@sswordistoolong1", False),
        ("Pass@word1", True),
        ("Password1", False),
        ("pass@word1", False),
        ("Pass@word", False)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

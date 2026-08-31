import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    (
        ("Pass@word1", True),
        ("qwerty", False),
        ("S1r@ng", False),
        ("Pass@word1Pass@word1", False),
        ("S1rongpass", False),
        ("-Password", False),
        ("-1srongpass", False),
        ("1111111111", False),
    )
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) is result

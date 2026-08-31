import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Qwer!y1", False),
        ("!Str@ngButT00Long!", False),
        ("Justaw@rd", False),
        ("just@w0rd", False),
        ("Justaw0rd", False)
    ]
)
def test_general_functionality(password: str, result: bool) -> None:
    assert check_password(password) is result

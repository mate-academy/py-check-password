import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Password&123", True),
        ("Password&12345678sd", False),
        ("Pass2&", False),
        ("Password&", False),
        ("Password123", False),
        ("password&123", False),
        ("пароль123&", False),
    ],
    ids=[
        "Should return True when follow all conditions",
        "Should return False for password with len > max_len",
        "Should return False for password with len < min_len",
        "Should return False for password with no digit",
        "Should return False for password with no special character",
        "Should return False for password with no letter in uppercase",
        "Should return False for password with invalid symbol",
    ]
)
def test_should_return_following_conditions(
        password: str,
        result: bool
) -> None:
    assert check_password(password) is result

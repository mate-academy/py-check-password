import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result", [
        ("Pass@word1", True),
        ("Password123", False),
        ("password7!", False),
        ("Password$", False),
        ("sHort3!", False),
        ("T00longpassword!!", False),
        ("with space", False)
    ]
)
def test_check_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result

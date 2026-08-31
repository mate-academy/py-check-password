import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_valid",
    [
        ("вхіахвх[[[]", False),
        ("a1_A", False),
        ("aasdasd1_", False),
        ("a1_A" * 9, False),
        ("a1A" * 3, False),
        ("aA_" * 3, False),
        ("1aaA_aaa", True)
    ]
)
def test_check_password(password: str,
                        is_valid: bool) -> None:
    assert check_password(password) is is_valid

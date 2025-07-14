import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "incoming_password,expected_result",
    [
        ("S3cur!ty79", True),
        ("Bright8@", True),
        ("Brighter_Thund3r", True),
        ("Unqu3st!on@b1l1ty9", False),
        ("password_228", False),
        ("k9@в7M2!", False),
        ("Best_password", False),
        ("Fast2025Run", False)
    ]
)
def test_should_return_correct_check(
    incoming_password: str,
    expected_result: bool
) -> None:
    assert check_password(incoming_password) == expected_result

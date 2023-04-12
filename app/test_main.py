import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("12345678", False),
        ("a$A12345678", True),
        ("a@A12345678", True),
        ("a A12345678", False),
        ("A12@", False),
        ("a$A123456789q1234", False),
        ("a$A123456789q123", True),
        ("aA123456789q123", False),
        ("a$a123456789q123", False)
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert (
        check_password(password) == expected_result
    ), f"{password} is {'valid' if expected_result else 'invalid'}"

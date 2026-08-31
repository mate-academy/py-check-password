import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("@Abcde7", False),
        ("@Abcdefg123456789", False),
        ("@abcdefg78", False),
        ("@Abcdefghi", False),
        ("Abcdefg789", False),
        ("@@@@@@A1", True),
        ("@@@@@@@@@@@@@@A1", True),
        ("@Abcdef1", True),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

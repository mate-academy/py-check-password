import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("Dawid12345#", True),

        ("Daw@1", False),
        ("password@1", False),
        ("A" * 17 + "1@", False),
        ("Password1", False),
        ("Password#", False),
        ("Pass word#", False),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    result = check_password(password)
    assert result == expected

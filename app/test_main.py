import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("A1$bcdEf", True),
        ("Abcdef1@", True),
        ("Strong_P@ss1", True),
        ("Valid#Pass123", True),

        ("Short1@", False),
        ("ThisPasswordIsWayTooLong1@", False),

        ("password1@", False),
        ("PASSWORD@", False),
        ("Password1", False),
        ("pass@word1", False),

        ("Pass word1@", False),
        ("Passçword1@", False),
        ("Pa$$wörd1", False),
        ("Password1%", False),

        # ✅ Limite superior (16)
        ("Valid#Pass123456", True),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    result = check_password(password)
    assert result is expected

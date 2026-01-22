import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("A@bcdef1", True),
        ("A@bcdefghijklm1", True),
        ("Aa1$bcdef", True),
        ("Aa1#bcdef", True),
        ("Aa1&bcdef", True),
        ("Aa1!bcdef", True),
        ("Aa1-bcdef", True),
        ("Aa1_bcdef", True),

        ("A@bcde1", False),
        ("A@bcdefghijklmno1", False),

        ("pass@word1", False),
        ("Pass@word", False),
        ("Passw0rd", False),

        ("Pass word1@", False),
        ("Пароль1@", False),
        ("Pass*word1", False),
        ("Pass{word1", False),
        ("Pass}word1", False),

        ("Password", False),
        ("12345678", False),
        ("$@#&!-_$", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

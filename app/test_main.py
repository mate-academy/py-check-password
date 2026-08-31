import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("NoSpecialChar1", False),
        ("NoDigit@", False),
        ("nouppercase@1", False),
        ("Pass_word12345!", True),
        ("Short1@", False),
        ("Valid1$Pass", True),
        ("NodigitAndSpecial!", False),
        ("UPPERCASE$1", True),
        ("lowercaseonly@1", False),
        ("S@meRealyVeryL0ngPasswordonly", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

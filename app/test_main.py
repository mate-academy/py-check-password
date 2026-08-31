import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param(
            "abc1@De",
            False,
            id="password is invalid when has less than 8 characters"
        ),
        pytest.param(
            "abc2$Defghijklmno",
            False,
            id="password is invalid when has more than 16 characters"
        ),
        pytest.param(
            "abc3#defg",
            False,
            id="password is invalid when doesn't have uppercase letter"
        ),
        pytest.param(
            "abc&Defg",
            False,
            id="password is invalid when doesn't have digit"
        ),
        pytest.param(
            "abcD4efghi",
            False,
            id="password is invalid when doesn't have special character"
        ),
        pytest.param(
            "abcD5!efGя",
            False,
            id="password is invalid when has non-Latin letter"
        ),
        pytest.param(
            "ab6Cd.efg",
            False,
            id="password is invalid when has invalid special character"
        ),
        pytest.param(
            "ab7Cd-_efg",
            True,
            id="password is valid when all rules are followed"
        ),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

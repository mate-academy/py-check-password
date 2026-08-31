import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("asc_q1@Werty", True),
        ("Pass@qwerty", False),
        ("Лщs@qwerty", False),
        ("asc_q1Wertyrrrrrr", False),
        ("P1@w", False),
        ("pass@word1", False),
        ("ascq1Werty", False),
    ]
)
def test_correct_password_check(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result

import pytest
from app.main import check_password


def test_len() -> None:
    assert check_password("Q1!4567") is False
    assert check_password("Q1!456789101234567") is False
    assert check_password("Q1!45678") is True
    assert check_password("Q1!4567890123456") is True
    assert check_password("Їщ1#qweqweqwe") is False


@pytest.mark.parametrize(
    "pass_example, expected_result",
    [
        ("Q14567890", False),
        ("q!1456789", False),
        ("Qqqqqqqqqqq", False),
        ("111111111111", False),
        ("$@#&!-_$@#&!-_", False),

    ]
)
def test_(pass_example: str, expected_result: bool) -> None:
    assert check_password(pass_example) == expected_result

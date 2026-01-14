import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("@1asdfasdf", False),
        ("@ASDfasdf", False),
        ("1ASDFasdf", False),
        ("@1ASDFasdfasdfasdf", False),
        ("@1ASDF", False),
        ("@1ASDFasdf", True)
    ],
    ids=[
        "no_upper",
        "no_digit",
        "no_special_character",
        "length_more_than_16",
        "length_less_than_8",
        "correct_password"
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

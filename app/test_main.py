import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,output",
    [
        ("Pass@word1", True),
        ("Pass@word_is_too_long_1", False),
        ("Short@1", False),
        ("Pass@word1%", False),
        ("Pass@word", False),
        ("Password1", False),
        ("pass@word1", False),
    ],
    ids=[
        "Valid password",
        "More than 16 characters",
        "Less than 8 characters",
        "Non ASCII characters",
        "Does not have at least one digit",
        "Does not have at least one special character",
        "Does not have at least one uppercase letter",
    ]
)
def test_check_password(
        password: str,
        output: bool
) -> None:
    assert check_password(password) is output

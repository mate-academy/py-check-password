from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Pass@1", False),
        ("Pass@word1Pass@word1", False),
        ("Password", False),
        ("pass@word1", False),
        ("Pass@word", False),
        ("Password1", False)
    ],
    ids=[
        "Correct password",
        "Too short password",
        "Too long password",
        "Use special characters and numbers",
        "Use >=1 capital letter",
        "Use >=1 number",
        "Use >=1 special characters"
    ]
)
def test_main(password: str, result: bool) -> None:
    assert check_password(password) == result

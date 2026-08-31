import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("P@5s", False),
        ("Pa55word@", True),
        ("passwordPa55word@", False),
        ("pa55word@", False),
        ("Password@", False),
        ("Pa55word", False)
    ],
    ids=[
        "Short password",
        "Correct password",
        "Password more than 16 symbols",
        "Without uppercase letter",
        "Without digits",
        "Without spacial symbols"
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

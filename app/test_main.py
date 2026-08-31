import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Saddfffjj@jkuyhjk", False),
        ("Qwerty@", False),
        ("Qwerasd$", False),
        ("Qw@1", False),
        ("asdf12##", False),
        ("QWas1233442$$#KKKKk", False)
    ],
    ids=[
        "Test correct password",
        "Test when len is low and without special char",
        "Test when len is low",
        "Test when len is too big",
        "Test without digits",
        "Should returns False for passwords without digits",
        "False when password is short",
        "Passwords without uppercase letter",
        "False for too long passwords"
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

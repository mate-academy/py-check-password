import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "word,output",
    [
        ("Pass@word1", True),
        ("Pas1@", False),
        ("qwerty", False),
        ("Qwerty62@jdkcmpwpdmxk", False),
        ("Passw@rd", False),
        ("password12@", False),
        ("Password1", False)
    ],
    ids=(
        "password is valid",
        "password it too short",
        "password does not match any of rules",
        "password should be any longer than 16 characters",
        "password must have digits",
        "need to have upper letter",
        "there might be a special symbol"
    )
)
def test_password(
        word: str,
        output: bool
) -> None:
    assert check_password(word) == output

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("P@ssword1", True),
        ("Pswrd!3", False),
        ("#TooLongPassword8", False),
        ("Qwerty^78", False),
        ("M@te@c@demy", False),
        ("IL0veMyCat", False),
        ("my7p#ssword", False),
        ("123$@#&!-_", False),
        ("МійП@роль123", False),
    ],
    ids=[
        "correct password",
        "too few characters",
        "too many characters",
        "not allowed special character",
        "no digits",
        "no special characters",
        "no uppercase letters",
        "no letters",
        "cyrillic letters"
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

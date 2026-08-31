import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result, message", [
        ("Ab!4-qep", True, "Status Ok, but ..."),
        ("A1!", False, "Password is short"),
        ("jdnaisdnjNSAJdni712787128&&", False, "Password to long"),
        ("asdf67$$", False, "Password without uppercase letter."),
        ("njNJnjp&", False, "Password without digits."),
        ("shAbau12345", False, "Password without special simbols.")
    ]
)
def test_check_password(
        password: str,
        result: bool,
        message: str) -> None:

    assert check_password(password) == result, message

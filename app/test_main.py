import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Passw0rd!", True),
        ("Secur3&$", True),
        ("P@ssw0rd", True),
        ("Ch@ll3nge", True),
        ("Str0ngP@$$", True),
        ("S3cur3&!", True),
        ("P@ssw0rd1", True),
        ("$tr0ngP@$$", True),
        ("MyP@$$w0rd", True),
        ("H3ll0W0rld!", True),
        ("password", False),
        ("12345678", False),
        ("P@ss", False),
        ("1!aA", False),
        ("Abcdefghijklmnopqrsta134!!!", False),
        ("1234abcd", False),
        ("iloveyou", False),
        ("qweRty", False),
        ("p@ssw0rd", False),
        ("S3cur3", False),
        ("PasswOrd!", False),
        ("Chall3nge", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

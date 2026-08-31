import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("$@#&!-_@@1P", True),
        ("$@#&!-_@@", False),
        ("Pas_words1password", False),
        ("pa$$wird1", False),
        ("@n1Me", False),
        ("qWerty1wfsd", False),
        ("Pa$$word", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

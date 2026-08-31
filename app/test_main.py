import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "passwort_example,result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng1", False),
        ("password", False),
        ("Pass@wordPa22word", False),
        ("pass@word1", False),
        ("Password1", False),
        ("Pass#word", False),
    ]
)
def test_check_password(passwort_example, result):
    assert check_password(passwort_example) == result

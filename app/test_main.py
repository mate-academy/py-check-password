import pytest

from app.main import check_password


@pytest.mark.parametrize("password,expected", [
    pytest.param(
        "Pass@word1", True,
        id="should pass all validation rules"
    ),
    pytest.param(
        "Pass@word1ж", False,
        id="should not contain non-Latin letters"
    ),
    pytest.param(
        "Pass@word1%<>/", False,
        id="should not contain special character except `$@#&!-_`"
    ),
    pytest.param(
        "Pass@1", False,
        id="should be at least 8 characters long"
    ),
    pytest.param(
        "Pass@word11234567", False,
        id="should not be longer than 16 characters inclusive"
    ),
    pytest.param(
        "Pass@word", False,
        id="should contain at least 1 digit"
    ),
    pytest.param(
        "Password1", False,
        id="should contain at least 1 special character"
    ),
    pytest.param(
        "pass@word1", False,
        id="should contain at least 1 uppercase letter"
    ),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected

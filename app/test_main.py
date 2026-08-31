import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password, walid",
    [
        pytest.param(
            "Pass@word1", True
        ),
        pytest.param(
            "qw!2tyaaa", False,
            id="password should have 1 uppercase letter"
        ),
        pytest.param(
            "St1@ng", False,
            id="password should have at least 8 characters"
        ),
        pytest.param(
            "St1aaang", False,
            id="password should have special character from $@#&!-_"
        ),
        pytest.param(
            "St!!!!ngaaa", False,
            id="password should have digits 0-9"
        ),
        pytest.param(
            "QQQ!!!1213ыЫ", False,
            id="password accepts only letters of the Latin alphabet Aa-Zz"
        ),
        pytest.param(
            "Passwordpassword!!1234", False,
            id="password should have maximum 16 characters inclusive"
        ),
    ]
)
def test_check_password(password: str, walid: bool) -> None:
    assert check_password(password) == walid

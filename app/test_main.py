import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param(
            "P@ss111",
            False,
            id="Should return 'false' if password shorter than 8 symbols"
        ),
        pytest.param(
            "Super_l0ng_psswrd",
            False,
            id="Should return 'false' if password longer than 16 symbols"
        ),
        pytest.param(
            "Just_password",
            False,
            id="Should return 'false' if password doesn't have digits"
        ),
        pytest.param(
            "Justp4ssword",
            False,
            id="Should return 'false' if password doesn't have specials"
        ),
        pytest.param(
            "just_p4ssword",
            False,
            id="Should return 'false' if password doesn't have uppers"
        ),
        pytest.param(
            "Just_p4ssword?",
            False,
            id="Should return 'false' if password have incorrect specials"
        ),
        pytest.param(
            "Just_p4ssword",
            True,
            id="Should return 'true' if password pass all validations"
        ),
    ]
)
def test_check_password_correctly(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Pass@word1",
            True,
            id=""
        ),
        pytest.param(
            "Pass@word1" * 10,
            False,
            id="should return `False` if the password is to long"
        ),
        pytest.param(
            "qwerty_ASDF",
            False,
            id="should return `False` if the password has no numbers"
        ),
        pytest.param(
            "qwerty12ASDF",
            False,
            id="should return `False` if the password has no special symbols"
        ),
        pytest.param(
            "12str@ng",
            False,
            id="should return `False` if the password has no uppercase letter"
        ),
        pytest.param(
            "Str@ng1",
            False,
            id="should return `False` if the password is to short"
        ),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Passw@ord1", True),
        ("12Password", False),
        ("Pass@word", False),
        ("1234567@#$", False),
        ("!@#$%%^&@#$", False),
        ("Pass1@", False),
        ("PassPas1@sPassPassPassPass", False)
    ]
)
def test_password_should_be_correct(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result

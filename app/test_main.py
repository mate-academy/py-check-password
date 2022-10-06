from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "passw,result",
    [
        pytest.param(
            "qwerty",
            False,
            id=("password should have at least 1 digit,"
                " 1 special character, 1 uppercase letter.")
        ),
        pytest.param(
            "Str@ng",
            False,
            id="password should have 1 diggits and and min 8 char"
        ),
        pytest.param(
            "Str@ng1",
            False,
            id="password whould have min 8 char"
        ),
        pytest.param(
            "Qwertyzzzzzzzzzz@12",
            False,
            id="password whould have max 16 char"
        ),
        pytest.param(
            "Pass@word1",
            True,
            id="Correct password"
        ),
        pytest.param(
            "Correct_pass",
            False,
            id="password should have diggit"
        ),
        pytest.param(
            "qwerty_123",
            False,
            id="password should have upper letter"
        )
    ]
)
def test_check_password(passw: str, result: bool):
    assert check_password(passw) is result

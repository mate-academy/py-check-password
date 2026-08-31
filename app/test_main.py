import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password_to_check, expected_answer",
    [
        pytest.param(
            "Abc!1234",
            True,
            id="Should return True"
        ),
        pytest.param(
            "Abc!123",
            False,
            id="Should return that password is too short"
        ),
        pytest.param(
            "Abc!123123123123321123",
            False,
            id="Should return that password is too long"
        ),
        pytest.param(
            "abc!1234",
            False,
            id="Should return that password has no uppercase letter"
        ),
        pytest.param(
            "Abc!abcd",
            False,
            id="Should return that password has no digits"
        ),
        pytest.param(
            "Abc12345",
            False,
            id="Should return that password has no special character"
        )
    ]
)
def test_password_checking(
        password_to_check: str,
        expected_answer: bool
) -> None:
    assert check_password(password_to_check) == expected_answer

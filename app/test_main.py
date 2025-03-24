import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="test correct password"
        ),
        pytest.param(
            "qwertyasd",
            False,
            id="test no digits and special character"
        ),
        pytest.param(
            "Str@nggggg",
            False,
            id="test no digits"
        ),
        pytest.param(
            "CorrectPassword@123!-butToLong",
            False,
            id="test password is too long"
        ),
        pytest.param(
            "Cg@1",
            False,
            id="test password is too short"
        ),
        pytest.param(
            "C@1aaaaaa",
            True,
            id="test at least 1 digit, 1 special character, 1 uppercase letter"
        ),
        pytest.param(
            "",
            False,
            id="test empty password line"
        ),
        pytest.param(
            "F123Hello",
            False,
            id="test witout special characters"
        ),
        pytest.param(
            "@hello123",
            False,
            id="test witout uppercase letter"
        ),
    ]
)
def test_check_password(
        password: str,
        result: bool) -> None:
    assert check_password(password) == result

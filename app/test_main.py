import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "МійПароль1@",
            False,
            id="Password shouldn't contain non Latin letters",
        ),
        pytest.param(
            "qw@4567",
            False,
            id="Password should contain at least 8 characters",
        ),
        pytest.param(
            "123456Q@",
            True,
            id="Valid password should be accepted",
        ),
        pytest.param(
            "$@#456789Qwertyu",
            True,
            id="Password should accept length up to 16",
        ),
        pytest.param(
            "$@#456789Qwertyu1",
            False,
            id="Password shouldn't contain more than 16 characters",
        ),
        pytest.param(
            "12345678",
            False,
            id="Password should contain at least "
               "one uppercase letter and special character",
        ),
        pytest.param(
            "Qwertyui",
            False,
            id="Password should contain at least "
               "one digit and special character",
        ),
        pytest.param(
            "12345Qwer",
            False,
            id="Password should contain at least one special character",
        ),
        pytest.param(
            "@!#$%^&*",
            False,
            id="Password should contain at least "
               "one digit and uppercase letter",
        ),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

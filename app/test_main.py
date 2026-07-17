import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "",
            False,
            id="empty password"
        ),
        pytest.param(
            "Asd1@va",
            False,
            id="password less than 8 characters"
        ),
        pytest.param(
            "Asd1@vai",
            True,
            id="password 8 characters"
        ),
        pytest.param(
            "Asd1@vaiAsd1@vai",
            True,
            id="password 16 characters"
        ),
        pytest.param(
            "Asd1@vaiAsd1@vai5",
            False,
            id="password more than 16 characters"
        ),
        pytest.param(
            "Asd@vaiAsd@vai",
            False,
            id="password without digits"
        ),
        pytest.param(
            "Asd1vaiAsd5vai",
            False,
            id="password without special characters"
        ),
        pytest.param(
            "sd1v$ai!sd5vai",
            False,
            id="password without uppercase letters"
        ),
        pytest.param(
            "Asdf@67Jю",
            False,
            id="password with non Latin letters"
        ),
        pytest.param(
            "Asdf@67J.",
            False,
            id="password with non permitted special characters"
        ),
    ]
)
def test_validate_passwords_correctly(
        password: str,
        expected: bool
) -> None:
    assert check_password(password) == expected

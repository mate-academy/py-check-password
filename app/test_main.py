import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="password with special character from the white list"
        ),
        pytest.param(
            "Jovanio231;",
            False,
            id="password with character not from white list"
        ),
        pytest.param(
            "jovanio2@2",
            False,
            id="password without uppercase letter"
        ),
        pytest.param(
            "Jovanio231@123441234124",
            False,
            id="password with more than 16 characters length"
        ),
        pytest.param(
            "Jov@1",
            False,
            id="password with less than 8 characters length"
        ),
        pytest.param(
            "Jovani123",
            False,
            id="password without special character from white list"
        ),
        pytest.param(
            "Jovani@@@",
            False,
            id="password without digits"
        )
    ]
)
def test_check_password(
        password: str,
        expected: bool
) -> None:
    assert check_password(password) == expected

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param(
            "1@Asd", False,
            id="Min len password is incorrect"
        ),
        pytest.param(
            "wwert5yuiopWWa@sdfghghgh", False,
            id="Max len password is incorrect"
        ),
        pytest.param(
            "Str@ng", False,
            id="Special symbols incorrect"
        ),
        pytest.param(
            "qwer@1ty", False,
            id="Only lowercase"
        ),
        pytest.param(
            "Pass@word1", True,
            id="Contain special symbols and uppercase"
        ),
        pytest.param(
            "Pass@word", False,
            id="Passwords without digits"
        ),
    ]
)
def test_password(password: str, result: bool) -> None:
    assert check_password(password) == result

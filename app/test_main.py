import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Pas@wo1",
            False,
            id="length should be bigger then 7"),
        pytest.param(
            "P@ss1word!-12qwop",
            False,
            id="length should be less then 17"),
        pytest.param(
            "Pass@word",
            False,
            id="Should contain at least one digit"),
        pytest.param(
            "Pass1word",
            False,
            id="Should contain at least one special charter"),
        pytest.param(
            "p@ss1word",
            False,
            id="Should contain at least one upper case letter"),
    ]
)
def test_check_password(password: str, expected: str) -> None:
    assert check_password(password) == expected

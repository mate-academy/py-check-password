import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("Pa@1", False, id="Password < min length"),
        pytest.param(
            "Pass@word1Pass@word1Pass@word1",
            False,
            id="Password > max length"),
        pytest.param(
            "Password1",
            False,
            id="Password without special symbols"),
        pytest.param("Pass@word", False, id="Password without numbers"),
        pytest.param("pass@word1", False, id="Password lower cased"),
        pytest.param("Pass@word1", True, id="Password is ok")
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

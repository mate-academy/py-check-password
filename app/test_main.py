import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "in_pass, result",
    [
        pytest.param(
            "Pass@word1", True,
            id="Password is correct"
        ),
        pytest.param(
            "qwerty", False,
            id="Password is incorrect"
        ),
        pytest.param(
            "Str@ng", False,
            id="Password is incorrect"
        ),
        pytest.param(
            "1S@s", False,
            id="Password is incorrect"),
        pytest.param(
            "Pass@word1Pass@word1Pass@word1", False,
            id="Password is incorrect"),
        pytest.param(
            "Password1P", False,
            id="Password is incorrect"),
        pytest.param(
            "@assword1s", False,
            id="Password is incorrect"),
        pytest.param(
            "Password@PSs", False,
            id="Password is incorrect"),
    ]
)
def test_check_password(in_pass: str,
                        result: bool) -> None:
    assert check_password(in_pass) == result

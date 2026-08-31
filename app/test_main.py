import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="Return true if all rules are covered"
        ),
        pytest.param(
            "Pass@word19999999999999999",
            False,
            id="Return false if password is too long"
        ),
        pytest.param(
            "Pass@word",
            False,
            id="Return false if password has no digits"
        ),
        pytest.param(
            "Pass@1",
            False,
            id="Return false if password is too short"
        ),
        pytest.param(
            "password@1",
            False,
            id="Return false if password has no uppercase letter"
        ),
        pytest.param(
            "Password1",
            False,
            id="Return false if password without special symbols"
        ),
    ]
)
def test_correct_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result

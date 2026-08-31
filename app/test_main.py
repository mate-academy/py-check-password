import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="password is valid"
        ),
        pytest.param(
            "password",
            False,
            id="password is not correct"
        ),
        pytest.param(
            "StrongPassword1",
            False,
            id="password is not correct"
        ),
        pytest.param(
            "Short1!",
            False,
            id="password is not correct"
        ),
        pytest.param(
            "short11!",
            False,
            id="password is not correct"
        ),
        pytest.param(
            "Tolongpassword11!",
            False,
            id="password is not correct"
        ),
        pytest.param(
            "Nodigits!",
            False,
            id="password is not correct"
        )
    ]
)
def test_check_password(
    password: str,
    expected_result: bool
) -> None:

    result = check_password(password)
    assert result == expected_result, (
        f"Expected result: {expected_result}, "
        f"Actual result: {result}"
    )

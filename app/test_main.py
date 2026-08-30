import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "",
            False,
            id="Empty string cannot be a password"
        ),
        pytest.param(
            "(123Dfgdffgffgh@",
            False,
            id="Inappropriate symbol in password"
        ),
        pytest.param(
            "123dfgdffghfgh@",
            False,
            id="No uppercase letter"
        ),
        pytest.param(
            "123Dfgdffgffgh",
            False,
            id="No special symbol"
        ),
        pytest.param(
            "Dfgdffghgfgh@",
            False,
            id="No digits"
        ),
        pytest.param(
            "1Gh@",
            False,
            id="Password is too short"
        ),
        pytest.param(
            "1Gh@dfgdfhgfhfjhjdyujhdhsdh",
            False,
            id="Password is too long"
        ),
        pytest.param(
            "123Dfgdffghffgh@",
            True,
            id="Maximum characters"
        ),
        pytest.param(
            "123Dfgd@",
            True,
            id="Minimum characters"
        ),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

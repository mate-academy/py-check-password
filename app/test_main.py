import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    (
        pytest.param("Pass@word1", True, id="Valid password"),
        pytest.param("qwerty", False),
        pytest.param("S1r@ng", False),
        pytest.param("too_long1@TOO_long2_passwords", False),
        pytest.param("NO1special", False),
        pytest.param("S-pecial", False),
        pytest.param("1", False, id="Short passwords"),
        pytest.param("no_uppercase2", False),
    )
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

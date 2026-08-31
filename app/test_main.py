import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("C0rrect_password", True),
        ("Wr0ng_к_password", False),
        ("Wr0ng", False),
        ("Wr0ng_passwordddd", False),
        ("Wrong_password", False),
        ("Wr0ng password", False),
        ("wr0ng_password", False),
        ("wrong password", False),
        ("Wr0ng>password", False),
    ]
)
def test_values(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result

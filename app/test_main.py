import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "current_pass,exception_rate",
    [
        ("P0ssw@rd", True),
        ("passw@rd1", False),
        ("pa@a", False),
        ("Paaaaaaa1aaaasw@rd", False),
        ("pass!1wrdD", True),
        ("PASSsw0rd@", True),
        ("Passw1rddd", False),
        ("Passw@rllld", False),
        ("Paw@rd1", False)
    ]
)
def test_check_password(
        current_pass: str,
        exception_rate: bool
) -> None:
    assert check_password(current_pass) == exception_rate

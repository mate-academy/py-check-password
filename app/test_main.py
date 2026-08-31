import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("aB3!", False),
        ("nhaaaaaB3", False),
        ("nhaaaaaB!", False),
        ("nhaaaab3!", False),
        ("Spam2pam@pamSPAM666", False),
        ("nOrma1p@rol", True)
    ]
)
def test_check_password(
        password: str,
        result: bool) -> None:

    assert (
        check_password(password) == result
    )

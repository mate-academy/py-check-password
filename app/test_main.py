import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "arg1, arg2",
    [
        ("vAl#e1", False),
        ("valu2E", False),
        ("va2@Eede", True),
        ("vae@Eede", False),
        ("vae2Eede", False),
        ("va2@eede", False),
        ("vAlu#eedewdew5", True),
        ("vAl2e@dewdew5dsdsd", False),
    ]
)
def test_check_password(arg1: str, arg2: bool) -> None:
    assert check_password(arg1) == arg2

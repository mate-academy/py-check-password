import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Sho1rt!", False),
        ("rr1Wetwtwr", False),
        ("Message1istoo@long", False),
        ("dfgdfggdQ!$@", False),
        ("dfsfs1g#sfsg", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

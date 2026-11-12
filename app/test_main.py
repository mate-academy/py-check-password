from app import main
import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("PASS@WORD1", True),
        ("Pas@wo1", False),
        ("Pass@word012345678", False),
        ("qwerty", False),
        ("Pass@wordd", False),
        ("Passwordd1", False),
        ("pass@word1", False),
        ("Pass@%+word1", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert main.check_password(password) == result

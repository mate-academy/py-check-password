import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("qwerty", False),
        ("qwerty_qwerty_qwe", False),
        ("фцацфафца", False),
        ("Qwe1rty$@#&!-_", True),
        ("qwerty$@#&!-_", False),
        ("qwerty^", False),
        ("qwerty$@", False),
        ("Qwerty$@", False),
        ("Qwerty$@1", True),
        ("Qweвrty$@1", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

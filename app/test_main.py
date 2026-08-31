import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Iamt00LooooongPassword!!!!!!helpme", False),
        ("onlyChars!", False),
        ("Ac1!", False),
        ("WithoutSpec1al", False),
        ("nouppercase01!", False)
    ],
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

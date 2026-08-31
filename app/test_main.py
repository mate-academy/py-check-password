import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("S9r@ng", False),
        ("Stttttgfgfgff88sdsdr@ng", False),
        ("fass@word1", False),
        ("PASDR8788@@D", True),
        ("PASDR8788D", False),
        ("PASDR@@@@D", False),
    ],
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

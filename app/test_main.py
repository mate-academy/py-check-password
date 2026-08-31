import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("P@wd1", False),
        ("Pass@word1Sdsdadw", False),
        ("qwerty@W", False),
        ("Str@ng", False),
        ("pass@word1", False)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, bool_value",
    [
        ("shgsdvE$", False),
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Ejdb5klha&hdiv5e8", False),
        ("#jasa5!!", False),
        ("A!1hi", False)
    ]
)
def test_check_password(password: str, bool_value: bool) -> None:
    assert check_password(password) == bool_value

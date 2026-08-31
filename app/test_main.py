import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected_output", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("Str@ng", False),
    ("M1t@", False),
    ("Qwertyu12345iopasd@09", False),
    ("Slava8Ukraini", False),
    ("Slava_Ukraini", False),
    ("67843750", False),
    ("gjhfsdg_58", False)]
)
def test_check_password(password: str, expected_output: bool) -> None:
    assert expected_output == check_password(password)

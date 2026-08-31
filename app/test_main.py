import pytest

from app.main import check_password


@pytest.mark.parametrize("password, expected_result", [
    ("Pass@word6", True),
    ("Sh@r7", False),
    ("More_than_16leta^rs", False),
    ("qwerty4#", False),
    ("Str@ng&&", False),
    ("Tes5Parollll", False),
    ("Long1rT$$n17le44ers", False),
])
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

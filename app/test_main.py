import pytest as pytest

from app.main import check_password


@pytest.mark.parametrize("password, expected_result", [
    ("Эыыыыыыыыыы", False),
    ("aaaaaaaa", False),
    ("aaaaaaaa1@", False),
    ("SSSwww@asasass", False),
    ("sssssSSSSS", False),
    ("SSSwww123@asasass", False),
    ("SSSwww123", False),
    ("Sw123@as", True),
    ("Pas@1as", False),

])
def test_password_check(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

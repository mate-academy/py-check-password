import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("_abracadabra1", False),
        ("_abracadabrA", False),
        ("abracadabrA1", False),
        ("_abracadabrA1_Gendolf_16", False),
        ("Ab_1", False),
        ("_abracadabrA1", True)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

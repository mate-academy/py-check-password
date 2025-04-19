import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "gotten_password,valid_password",
    [
        ("A1!qwer", False),
        ("A1!qwer2", True),
        ("A1aqwer2", False),
        ("A@!qwerq", False),
        ("a1!qwera", False),
        ("aaaaaaaa", False),
        ("A1!aaaaaaaaaaaaaa", False),
        ("A1!aaaaaaaaaaaaa", True),
        ("$@#&!-_1A", True),
        ("%^*()=+/.?>,<'A1", False),
        (";:|]}[{A1", False)
    ]
)
def test_function_gets_boundary_values(
        gotten_password: str,
        valid_password: bool
) -> None:
    assert check_password(gotten_password) == valid_password

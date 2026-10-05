import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("", False),
        ("A1@abcd", False),
        ("A1@abcde", True),
        ("A1@abcdefghijklm", True),
        ("A1@abcdefghijklmn", False),
        ("a1@abcde", False),
        ("A@abcdef", False),
        ("A1abcdef", False),
        ("A1@abcd ", False),
        ("A1@abcd%", False),
        ("A1@abcdé", False),
        ("A１@abcde", False),
        ("A²@abcde", False),
        ("A1@ABCDZ", True),
    ],
)
def test_password_rules(password: str, expected: bool) -> None:
    assert check_password(password) is expected


@pytest.mark.parametrize("special", list("$@#&!-_"))
def test_each_allowed_special_character(special: str) -> None:
    assert check_password(f"A1{special}abcde") is True

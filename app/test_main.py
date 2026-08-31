import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password,expected", [
        ("Pass@word1", True),
        ("Qw@rty1", False),
        ("Qwertyu12", False),
        ("STRONGSTRONG", False),
        ("&#^&@#!$^%$@", False),
        ("D@agysjdfuqyew123", False),
        ("qw@rty123", False),
        ("Qw@ertys", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Qwer1#", False),  # length < 8
        ("Qwer1#yycctfcfc17", False),  # length > 16
        ("Qwero#yycctfc", False),  # no digit
        ("Qwer12yycctfc15", False),  # no spec char
        ("qwer12#ycctfc15", False),  # no uppercase letter
        ("Qwer12/ yytfc15", False),  # illegal characters
        ("Qwer1#yycctfcf16", True),  # length = 16
        ("Pass@wo8", True),  # length = 8
        ("Qwer1#yctfcf16", True),  # 8 < length < 16
    ],
    ids=[
        "length < 8",
        "length > 16",
        "no digit",
        "no spec char",
        "no uppercase letter",
        "illegal characters",
        "Password Ok length = 16",
        "Password Ok length = 8",
        "Password Ok 8 < length < 16",
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

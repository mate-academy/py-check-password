from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "value, expectation",
    [
        ("A1&A0gd", False),
        ("супер_пас123@", False),
        ("WhatDoUThinkOfMyPass123@", False),
        ("H$@#&!-_", False),
        ("OneDigit0nly", False),
        ("HereisaP@ssw0rd", True),
    ]
)
def test_password(value: str, expectation: bool) -> None:
    assert expectation == check_password(value)

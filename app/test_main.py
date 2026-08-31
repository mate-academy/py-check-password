import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "passw, result",
    [
        ("zA1@", False),
        ("zA123asda_&$#@@@4@#$-_", False),
        ("zA1234@#$-%_", False),
        ("zAdf#d@f@#zx-_", False),
        ("12124$@#&&3233", False),
        ("hkhkjas3242AWkla", False),
        ("asasd23#@#_1q", False),
        ("zA1234@#$-wF_", True),
    ],
    ids=[
        "short passw",
        "long passw",
        "restricted spec",
        "no digit",
        "no alpha",
        "no spec",
        "no Upper",
        "good",

    ]
)
def test_can_check_password(
        passw: str,
        result: bool
) -> None:
    assert check_password(passw) == result

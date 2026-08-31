import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("P@ssw0rd", True),
        ("P@sw0rd", False),
        ("P@ssw0rdP@ssw0rd1", False),
        ("P@ssword", False),
        ("Passw0rd", False),
        ("p@ssw0rd", False),
        ("П@ssw0rd", False),
        ("P@ss^w0rd", False)
    ],
    ids=[
        "8-16 characters, 1 digit, 1 special, 1 uppercase",
        "7 characters",
        "17 characters",
        "no digit",
        "no special",
        "no uppercase",
        "cyrillic character",
        "forbidden special"
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

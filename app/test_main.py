import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Qrt1y@", False),
        ("Qrt1y@dsafdsafdsafdsafdasfdsfdsafdsaf", False),
        ("qwerty1@", False),
        ("Qwertyq@", False),
        ("Qwerty11", False),
        ("QWERTY1@", True),
    ],
    ids=[
        "correct password",
        "too short password",
        "too long password",
        "without upper letter",
        "without number",
        "without special symbol",
        "correct password with all letter upper"
    ]
)
def test_main(password: str, result: bool) -> None:
    assert check_password(password) is result

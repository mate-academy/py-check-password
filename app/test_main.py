import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("", False),
        ("Aw#scc2", False),
        ("ASdjfaS23#444132j", False),
        ("Asdff1263ggdb", False),
        ("ADASDA_#!SDgdb", False),
        ("asdlka211#!#@!", False),
        ("asaф211#!#@!", False),
        ("Asd@faw3ggdb", True)

    ],
    ids=[
        "Empty password",
        "Password length 7 characters",
        "Password length 17 characters",
        "Password without special characters",
        "Password without digits",
        "Password without uppercase letters",
        "Password contains non-ascii characters",
        "Password pass all requirements"
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result

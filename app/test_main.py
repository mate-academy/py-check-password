import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("", False),
        ("S67df@6", False),
        ("67hjS#gh", True),
        ("ghfghf678676D#@j", True),
        ("ghfghf678676D#@jh", False),
        ("gjkhkh678686D", False),
        ("ghgjg676#", False),
        ("DFHJhgh##@", False),
        ("fghD#@67ю", False)
    ],
    ids=[
        "check empty string",
        "check not enought lenght but all characters valid",
        "check minimal size",
        "check maximum size",
        "check too long password",
        "chech not using special caracter",
        "check not using uppercase letter",
        "check not using number",
        "check using not Latin alfabet"
    ]
)
def test_password_is_valid(password: str, result: bool) -> None:
    assert check_password(password) == result

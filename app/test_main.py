import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("TheBe@stpassw0rd", True),
        ("1234", False),
        ("Goodp@ssword", False),
        ("greatp@ssw0rd", False),
        ("Жоскийп@r0ль", False),
        ("Somewhatg00dpass", False)
    ],
    ids=[
        "check valid password",
        "password must contain letters from the Latin alphabet",
        "password must contain numbers",
        "password must contain upper case letter",
        "password must use only ASCII characters",
        "password must contain special character from `$@#&!-_`"
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

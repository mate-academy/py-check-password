import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Password1@", True),
        ("PasSSSSSSSSSSSSSSSSSSSSSsword1@", False),
        ("nouppercase1#", False),
        ("Pas$#$#$#$", False),
        ("ThisIsGoodPas1", False),
        ("Foo1#", False)
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

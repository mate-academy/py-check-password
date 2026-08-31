import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("12jF!", False),
        ("12jFgsdh", False),
        ("FEHJFHF!1", True),
        ("hgdfkghsd1!", False),
        ("String1", False),
        ("11iGg2i4u21hbhjb21jh!11111", False),
        ("String!!!", False),
        ("83IIIhhh!&", True),
        ("String1!!", True),
    ]
)
def test_check_password_works_correctly(
    password: str, result: bool
) -> None:
    assert check_password(password) == result

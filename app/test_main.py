import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("P!ass@wo1rd", True),
        ("Q!1rty", False),
        ("Qwer1#ty1111111111111", False),
        ("Str@nbbbg", False),
        ("p!ass@wo1r", False)
    ]
)
def test_should_check_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

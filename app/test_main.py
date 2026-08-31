import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("qwertyu", False),
        ("Qwerty1_", True),
        ("Qwerty1_ШЩ", False),
        ("1231411532", False),
        ("sf_wef_sfsfe", False),
        ("$@#&!-_$@#", False),
        ("DFSDFUSIDFHSF", False),
        ("1qW_", False),
        ("fsdfsdfsnfesfsdfsdfessdfs", False),
        ("QWErty_1_2", True)
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result

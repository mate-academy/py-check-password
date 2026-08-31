import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result_check",
    [
        ("Pass@word1", True),
        ("Sem1@senha1", True),
        ("A@g2", False),
        ("avbxAdssf", False),
        ("AvbxAdss7", False),
        ("AvbxAdss7dfjhidyhrejysfryku@12syjdf", False),
        ("dfghj#$183", False),
        ("Str@ngoi", False)
    ]

)
def test_correct_check_password(
    password: str,
    result_check: bool
) -> None:
    assert check_password(password) == result_check

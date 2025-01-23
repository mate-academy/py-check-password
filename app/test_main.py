from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("p1a_Wor", False),
        ("1Qwerkjfty", False),
        ("qwjert@74y", False),
        ("soMe_Password", False),
        ("jdhfu!jdfhjkkd1Ad", False),
        ("?somePas1w", False),
    ],
    ids=[
        "password with 1 digit, 1 special, 1 uppercase and 8-16 chars",
        "test password less than 8 chars",
        "test password without special char",
        "test password without upper char",
        "test password without digit",
        "test password more than 16 chars",
        "test password with wrong special char",
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

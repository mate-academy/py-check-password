from pytest import mark

from app.main import check_password


@mark.parametrize(
    "password, is_password",
    [
        ("Pass@word1", True),
        ("St1@ng", False),
        ("qwerty21@", False),
        ("Q@bhvdcfd", False),
        ("Q1rfggrjfgr", False),
        ("1@Dhnihvfubjgtutrhb", False)
    ]
)
def test_check_password(password: str, is_password: bool) -> None:
    assert check_password(password) == is_password

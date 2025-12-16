from app.main import check_password


def test_check_password() -> None:
    assert check_password("Pass@1") is False
    assert check_password("pass@word1") is False
    assert check_password("Password1") is False
    assert check_password("Pass@4Pass@4Pass@4Pass@4Pass@4") is False
    assert check_password("Pass@word") is False

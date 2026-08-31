from app.main import check_password


def test_check_password_corrected_result() -> None:
    assert check_password("ізщфівИ0!") is False
    assert check_password("") is False
    assert check_password("Pass@word1Pass@word1") is False
    assert check_password("Pass@word1") is True

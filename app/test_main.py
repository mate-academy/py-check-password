from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1")
    assert check_password("A1b@cdEf2G!")
    assert check_password("12345678@A")
    assert check_password("abcdefgh@A1")
    assert check_password("A1abcd!gmno")


def test_invalid_password() -> None:
    assert not check_password("shor1!A")
    assert not check_password("aB@1")
    assert not check_password("A1@longpassword1234!")
    assert not check_password("A1!b" * 5)
    assert not check_password("Abcdefgh!")
    assert not check_password("Abcdefgh1")
    assert not check_password("abcdefg1@")
    assert not check_password("Invalid1234")
    assert not check_password("Invalid@$%^!123")

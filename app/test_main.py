from app.main import check_password


def test_check_password() -> None:
    assert check_password("Pass@word1") is True
    assert check_password("qwerty") is False
    assert check_password("trong5@ssw") is False
    assert check_password("Str@ng") is False
    assert check_password("trongP@ssword") is False
    assert check_password("Short!2") is False
    assert check_password("Abcdefg1") is False
    assert check_password("Abcdefg1!") is True
    assert check_password("ShortPa$") is False
    assert check_password("LongPasswordWithAllRequirements1@") is False
    assert check_password("MissingUpper&Special1") is False
    assert check_password("TooLongPasswordWithAllRequirements1@#") is False
    assert check_password("InvalidPassword") is False
    assert check_password("ValidPa$$w0rd") is True
    assert check_password("Pa$$w0rdWithoUtSpec!al") is False
    assert check_password("Pa$$w0rdWithouT1") is True

from app.main import check_password


def test_too_short_len():
    assert check_password("Qaz_1qa") is False


def test_too_long_len():
    assert check_password("Qaz_1qa_Qaz_1qa_1") is False


def test_no_letters():
    assert check_password("1234567_@") is False


def test_no_uppercase_letters():
    assert check_password("123456a_@") is False


def test_no_digit():
    assert check_password("Awasdfg_@") is False


def test_no_special_character():
    assert check_password("Awasdfg12") is False


def test_password_is__ok():
    assert check_password("Awasdf_12") is True

from app.main import check_password


def test_correct_pass():
    assert check_password("Reallyg00dp@ss") is True


def test_empty_pass():
    assert check_password("") is False


def test_too_short_pass():
    assert check_password("as#Fs1") is False


def test_at_least_one_digit():
    assert check_password("greatpasASd_#") is False


def test_too_long_pass():
    assert check_password("123Verylong@pass$") is False


def test_no_upper_letters():
    assert check_password("alllowercase07$") is False


def test_no_special_symbol():
    assert check_password("Greatpass123pa") is False

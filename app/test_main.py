from app.main import check_password


def test_empty_string():
    assert check_password("") is False


def test_short_password():
    assert check_password("123Qw_") is False


def test_long_password():
    assert check_password("123qwAe123qw@Ae1239") is False


def test_no_upper():
    assert check_password("mateacademy3_") is False


def test_no_digit():
    assert check_password("MateAcademy_") is False


def test_no_special_character():
    assert check_password("MateAcademy3") is False


def test_valid_password():
    assert check_password("MateAcademy3_") is True

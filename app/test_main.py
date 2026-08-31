from app.main import check_password


def test_should_check_max_length():
    test_value1 = 'P@ssw0rd1Passw0rd12'
    assert check_password(test_value1) is False


def test_should_check_min_length():
    test_value2 = 'Qw@rt1'
    assert check_password(test_value2) is False


def test_has_upper():
    test_value = 'qw@rty123'
    assert check_password(test_value) is False


def test_has_digit():
    test_value = 'Str@ngeral'
    assert check_password(test_value) is False


def test_has_special():
    test_value = 'Passw0rd1'
    assert check_password(test_value) is False


def test_if_all_parameters_true():
    test_value = 'Pass@word1'
    assert check_password(test_value) is True

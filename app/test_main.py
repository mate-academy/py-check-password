import pytest
from app.main import check_password


@pytest.fixture()
def password():
    return "P@ssw0rd"


def test_should_check_min_length(password: str) -> bool:
    if len(password) < 8:
        return False
    has_upper = False
    has_digit = False
    has_special = False
    for letter in password:
        if letter.isalpha():
            if letter.upper() == letter:
                has_upper = True
        elif letter.isdigit():
            has_digit = True
        elif letter in "$@#&!-_":
            has_special = True
        else:
            return False
    return all([has_upper, has_digit, has_special])


def test_should_check_max_length(password: str) -> bool:
    if len(password) > 16:
        return False
    has_upper = False
    has_digit = False
    has_special = False
    for letter in password:
        if letter.isalpha():
            if letter.upper() == letter:
                has_upper = True
        elif letter.isdigit():
            has_digit = True
        elif letter in "$@#&!-_":
            has_special = True
        else:
            return False
    return all([has_upper, has_digit, has_special])


def test_should_check_upper_letter(password: str) -> bool:
    if len(password) not in range(8, 17):
        return False
    has_digit = False
    has_special = False
    has_upper = False
    for letter in password:
        if letter.isdigit():
            has_digit = True
        elif letter in "$@#&!-_":
            has_special = True
        elif letter.isalpha():
            if letter.upper() == letter:
                has_upper = True
            continue
        else:
            return False
    return all([has_digit, has_special, has_upper])


def test_should_check_digit(password: str) -> bool:
    if len(password) not in range(8, 17):
        return False
    has_upper = False
    has_special = False
    has_digit = False
    for letter in password:
        if letter.isalpha():
            if letter.upper() == letter:
                has_upper = True
        elif letter.isdigit():
            has_digit = True
            continue
        elif letter in "$@#&!-_":
            has_special = True
        else:
            return False
    return all([has_upper, has_special, has_digit])


def test_should_check_special_symbols(password: str) -> bool:
    if len(password) not in range(8, 17):
        return False
    has_upper = False
    has_digit = False
    has_special = False
    for letter in password:
        if letter.isalpha():
            if letter.upper() == letter:
                has_upper = True
        elif letter.isdigit():
            has_digit = True
        elif letter in "$@#&!-_":
            has_special = True
        else:
            return False
    return all([has_upper, has_digit, has_special])


def test_check_password(password):
    # password = ""
    has_len_min = \
        test_should_check_min_length("1@aA") == check_password("1@aA")
    has_upper = \
        test_should_check_upper_letter("1@a12345")\
        == check_password("1@a12345")
    has_digit = \
        test_should_check_digit("Q@asdfgh") == check_password("Q@asdfgh")
    has_special = \
        test_should_check_special_symbols(password) == check_password(password)
    has_len_max = \
        test_should_check_max_length("@QWERTYUIOPasdfghjkl12345678")\
        == check_password("@QWERTYUIOPasdfghjkl12345678")
    assert all([has_upper,
                has_digit,
                has_special,
                has_len_min,
                has_len_max]) is True

import re

from app.main import check_password


def test_valid_characters_ok() -> None:
    password = "Hello123_&"
    assert bool(re.match("^[a-zA-Z0-9$@#&!_]+$", password)) == \
           check_password(password)


def test_at_least_8_characters_ok() -> None:
    password = "Hello123_&"
    assert (len(password) >= 8) == check_password(password)


def test_at_least_8_characters_not_ok() -> None:
    password = "Hello1&"
    assert (len(password) >= 8) == check_password(password)


def test_maximum_16_characters_ok() -> None:
    password = "Hello123_&"
    assert (len(password) <= 16) == check_password(password)


def test_maximum_16_characters_not_ok() -> None:
    password = "Hello123_&34567898765432345678"
    assert (len(password) <= 16) == check_password(password)


def test_contains_necessary_charachters_ok() -> None:
    password = "Hello123_&"
    assert bool(
        re.match("[A-Z]+", password)
        and re.search("[0-9]+", password)
        and re.match("[$@#&!-_]+", password)) == check_password(password)


def test_lacks_necessaryuppercase_letter_not_ok() -> None:
    password = "hello123_&"
    assert ((re.search("[A-Z]+", password)
             and re.search("[0-9]+", password)
             and re.search("[$@#&!-_]+", password)) is not None) \
           == check_password(password)


def test_lacks_digits_not_ok() -> None:
    password = "Hello&jfds"
    assert ((re.search("[A-Z]+", password)
             and re.search("[0-9]+", password)
             and re.search("[$@#&!-_]+", password)) is not None) \
           == check_password(password)


def test_lacks_special_symbol_not_ok() -> None:
    password = "Hellogfdm12"
    assert any([letter for letter in password if letter in "$@#&!-_"]) \
           == check_password(password)

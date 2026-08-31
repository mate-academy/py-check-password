import pytest

from app import main


def test_should_check_min_length(monkeypatch):
    def check_without_min_length(password: str) -> bool:
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

    monkeypatch.setattr(main, "check_password", check_without_min_length)

    test_result = pytest.main(["app/test_main.py"])
    assert (
        test_result.value == 0
    ), "Tests should check that 'check_password' returns False for short passwords"


def test_should_check_max_length(monkeypatch):
    def check_without_max_length(password: str) -> bool:
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

    monkeypatch.setattr(main, "check_password", check_without_max_length)

    test_result = pytest.main(["app/test_main.py"])
    assert (
        test_result.value == 0
    ), "Tests should check that 'check_password' returns False for too long passwords"


def test_should_check_upper_letter(monkeypatch):
    def check_without_upper_letter_condition(password: str) -> bool:
        if len(password) not in range(8, 17):
            return False
        has_digit = False
        has_special = False
        for letter in password:
            if letter.isdigit():
                has_digit = True
            elif letter in "$@#&!-_":
                has_special = True
            elif letter.isalpha():
                continue
            else:
                return False
        return all([has_digit, has_special])

    monkeypatch.setattr(main, "check_password", check_without_upper_letter_condition)

    test_result = pytest.main(["app/test_main.py"])
    assert (
        test_result.value == 0
    ), "Tests should check that 'check_password' returns False for passwords without uppercase letter"


def test_should_check_digit(monkeypatch):
    def check_without_digit_condition(password: str) -> bool:
        if len(password) not in range(8, 17):
            return False
        has_upper = False
        has_special = False
        for letter in password:
            if letter.isalpha():
                if letter.upper() == letter:
                    has_upper = True
            elif letter.isdigit():
                continue
            elif letter in "$@#&!-_":
                has_special = True
            else:
                return False
        return all([has_upper, has_special])

    monkeypatch.setattr(main, "check_password", check_without_digit_condition)

    test_result = pytest.main(["app/test_main.py"])
    assert (
        test_result.value == 0
    ), "Tests should check that 'check_password' returns False for passwords without digits"


def test_should_check_special_symbols(monkeypatch):
    def check_without_special_symbols(password: str) -> bool:
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
        return all([has_upper, has_digit])

    monkeypatch.setattr(main, "check_password", check_without_special_symbols)

    test_result = pytest.main(["app/test_main.py"])
    assert (
        test_result.value == 0
    ), "Tests should check that 'check_password' returns False for passwords without special symbols"

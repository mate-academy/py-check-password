import pytest
from unittest import mock
from app.main import check_password


@pytest.fixture()
def test_chek_pass():
    with mock.patch("app.main.check_password") as mocked_test:
        yield mocked_test


def test_len(test_chek_pass):
    assert check_password("Pass@word1") is True


def test_without_charter():
    assert check_password("dsfsdfSD1") is False


def test_biggest_len():
    assert check_password("QWERTY@2133WRSfsfsd"
                          "fwqewqeqwewqe666") is False


def test_smallest_len():
    assert check_password("Qwe@rt3") is False


def test_digits():
    assert check_password("wqSwqe@weqweqw") is False


def test_upper():
    assert check_password("wqwqewe@we2") is False

from app.main import check_password

import pytest


@pytest.fixture
def data_for_test():
    return {
        "Pass@word1": True,
        "Qwertsdf@": False,
        "pass@word123": False,
        "P@1": False,
        "Pass@word1kaslkdfjjlsf": False,
        "S1trdng": False,
    }


def test_checks_password(data_for_test):
    for password, boolean in data_for_test.items():
        assert check_password(password) is boolean

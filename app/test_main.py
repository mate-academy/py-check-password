from app.main import check_password
import pytest


@pytest.fixture
def check_password_fixture() -> None:
    return check_password


def test_password_rules(check_password_fixture: str) -> None:
    assert check_password_fixture("Pass@word1") is True
    assert check_password_fixture("qwerty") is False
    assert check_password_fixture("Str@ng") is False
    assert check_password_fixture("VeryLongPassword123@") is False
    assert check_password_fixture("Password@") is False
    assert check_password_fixture("Password1") is False
    assert check_password_fixture("password1@") is False
    assert check_password_fixture("password") is False
    assert check_password_fixture("Password1!") is True
    assert check_password_fixture("Password1%") is False
    assert check_password_fixture("Abcdef@1") is True
    assert check_password_fixture("Abcde@1") is False

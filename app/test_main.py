import pytest
from app.main import check_password


@pytest.mark.parametrize("bad_password", [
    "StrongPass",
    "StrongPass123",
    "123strong_pass123",
    "1Мій_пароль_1",
    "qwerty",
    "Qwe1*"
])
def test_check_wrong_password(bad_password: str) -> None:
    assert check_password(bad_password) is False


@pytest.mark.parametrize("good_password", [
    "Pass@word1",
    "Strong_Pass123",
    "1stronG-Pass@",
    "sTRONg_pASs123"
])
def test_check_correct_password(good_password: str) -> None:
    assert check_password(good_password) is True

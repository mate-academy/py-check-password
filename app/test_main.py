import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param(
            "pass_word_123",
            False,
            id="False if don't have upper"
        ),
        pytest.param(
            "Pass_Word",
            False,
            id="False if don't have digits"
        ),
        pytest.param(
            "Пароль_123",
            False,
            id="False if not latin letters"
        ),
        pytest.param(
            "PassWord2024",
            False,
            id="False if no special"
        ),
        pytest.param(
            "Parol_1",
            False,
            id="False if less then 8 chars"
        ),
        pytest.param(
            "Ultra_Mega_Password_2024",
            False,
            id="False if more then 16 chars"
        ),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

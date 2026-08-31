import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("qwerty1", False),
        ("Str@qwertytworty25123ng", False),
        ("!qwerty@", False),
        ("qwertyuio@", False),
        ("QWERTYUIOPASDFGHJKLZXCVBNM12345", False),
        ("Qwertyu123!@#sswwssdwswsd", False),
        ("Qwerties#1ц", False),
        ("qwerties#1", False),
        ("Pass@word1", True),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

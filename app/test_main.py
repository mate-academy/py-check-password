import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_action",
    [
        ("Str@ng1", False),
        ("Qwerty@aser", False),
        ("Cucaracha", False),
        ("b@mbino1", False),
        ("Pipi1@pupuchecking", False),
        ("P@ssword1", True)
    ]
)
def test_check_password(password: str, expected_action: bool) -> None:
    result = check_password(password)

    assert result == expected_action

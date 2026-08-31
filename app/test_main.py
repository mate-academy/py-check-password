import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, bool_value",
    [
        ("Passw@rd12", True),
        ("123123", False),
        ("Passworddd@", False),
        ("password@1", False),
        ("pааssW@ed12", False),
        ("Рassword@1", False),

    ]
)
def test_check_password(password: str, bool_value: bool) -> None:
    assert check_password(password) == bool_value

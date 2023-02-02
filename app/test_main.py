import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "current_password, result",
    [
        ("", False),
        ("12345678", False),
        ("khmuravit", False),
        ("Khmura_vit", False),
        ("Vit@12", False),
        ("password@31", False),
        ("Password@forme14567", False),
        ("Pas@word12", True),
        ("Password_@145678", True)
    ]
)
def test_check_password(current_password: str, result: bool) -> None:
    assert check_password(current_password) == result

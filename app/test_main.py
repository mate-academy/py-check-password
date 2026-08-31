from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Python0128test", False),
        ("Pswrd1@", False),
        ("Python@128test128test128test128test", False),
        ("Python@@@@test", False),
        ("1ython@@@@test", False),
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result

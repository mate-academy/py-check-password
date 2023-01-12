import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Mypass1@", True),
        ("Mypas1@", False),
        ("Mypassword123456@", False),
        ("Mypass12", False),
        ("Mypass@_", False),
        ("mypass1@", False),
        ("Mypass1@%", False)
    ],
    ids=[
        "test_valid_password",
        "test_password_shorter_8",
        "test_password_longer_16",
        "test_password_without_special",
        "test_password_without_digits",
        "test_password_without_upper",
        "test_password_with_not_allowed_special"
    ]
)
def test_correct_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("", False),
        ("Dssdgsdg#", False),
        ("abracad#1", False),
        ("Organize1", False),
        ("Or$1", False),
        ("Orfgddfbhrfthtyjtyujtytyjn$1", False),
        ("SuperPass$1", True),
        (12243325, TypeError),
    ],
    ids=[
        "should return False with empty password",
        "should return False without digit",
        "should return False without upper",
        "should return False without special",
        "should return False with length less than 8",
        "should return False with length bigger than 16",
        "should return False with right password",
        "should return TypeError if password not a string",
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    if not isinstance(password, str):
        with pytest.raises(TypeError):
            check_password(password)
    else:
        assert check_password(password) == expected_result

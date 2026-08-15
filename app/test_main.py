import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Qw@1t", False),
        ("Str@n1ghrhrthrtrt", False),
        ("str@n1ghrhr", False),
        ("Str@naghrhr", False),
        ("Strgn1ghrhr", False),
        (1236548, TypeError),
    ]
    , ids=[
        "1 digit, 1 special character, 1 uppercase letter must be True",
        "if password <= 8 char must be False",
        "if password > 16 char must be False",
        "if password has not Uppercase char must be False",
        "if password has not digit must be False",
        "if password has not special char must be False",
        "if password not str type must be TypeError"
    ]

)
def test_check_password(password: str, result: bool | Exception) -> None:
    if isinstance(result, type) and issubclass(result, Exception):
        with pytest.raises(result):
            check_password(password)
    else:
        assert check_password(password) == result

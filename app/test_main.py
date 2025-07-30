import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param("Pass@word1", True,
                     id="contains at least 1 digit, 1 special character, 1 uppercase letter"),
        pytest.param("sqwer@2ty", False,
                     id="should contains at least 1 uppercase letter"),
        pytest.param("Str@ng7", False,
                     id="should contains at least 8 characters"),
        pytest.param("Str@ngmJsdnjfn877", False,
                     id="should contains maximum 16 characters"),
        pytest.param("Sess@aawFe", False,
                     id="should contains at least 1 digit"),
        pytest.param("Sess231jjdH", False,
                     id="should contains at least 1 special character"),
        pytest.param("Good@Пароль1", False,
                     id="contains Cyrillic letters"),
        pytest.param("Good@pass 1", False,
                     id="contains space"),
        pytest.param("Good*pass1", False,
                     id="contains invalid special symbol")
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

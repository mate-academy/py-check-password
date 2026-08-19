import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="password-'Pass@word1', result-True"
        ),
        pytest.param(
            "qwerty",
            False,
            id="password-'qwerty', result-False"
        ),
        pytest.param(
            "Sr@1ng",
            False,
            id="password-'Str@ng', result-False"
               "---too small---"
        ),
        pytest.param(
            "Passsjdhkdfgkdfjghaaa@word1",
            False,
            id="password-'Passsjdhkdfgkdfjghaaa@word1', "
               "result-False ---too long---"
        ),
        pytest.param(
            "pass@word1",
            False,
            id="password-'pass@word1', "
               "result-False ---without uppercase letter---"
        ),
        pytest.param(
            "Pass@wordd",
            False,
            id="password-'Pass@wordd', "
               "result-False ---without digits---"
        ),
        pytest.param(
            "Passwword1",
            False,
            id="password-'Passwword1', "
               "result-False ---without special symbols---"
        ),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

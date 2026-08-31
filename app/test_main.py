import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="password meet all requirements must be `True`"
        ),
        pytest.param(
            "Pass@word",
            False,
            id="password without number must be `False`"),
        pytest.param(
            "Password1",
            False,
            id="password without special symbol must be `False`"
        ),
        pytest.param(
            "pass@word1",
            False,
            id="password without upper letter must be `False`"
        ),
        pytest.param(
            "Пас@ворд1",
            False,
            id="password must be Latin Alphabet"),
    ],
)
def test_check_password_with_different_characters(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result

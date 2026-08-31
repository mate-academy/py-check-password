import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="should return true when password is correct"
        ),
        pytest.param(
            "qwerty",
            False,
            id="only letter return False"
        ),
        pytest.param(
            "Str@nggfhfh",
            False,
            id="without digit return False"
        ),
        pytest.param(
            "Password123",
            False,
            id="without special character return False"
        ),
        pytest.param(
            "12345123",
            False,
            id="only digits return False"
        ),
        pytest.param(
            "Book12@",
            False,
            id="len < 8 return False"
        ),
        pytest.param(
            "book12H@readkitchen",
            False,
            id="len > 16 return False"
        ),
        pytest.param(
            "book12@34g",
            False,
            id="without upper letter return False"
        )
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

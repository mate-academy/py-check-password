import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param("Pass@word1", True, id="correct password"),
        pytest.param("qwerty12!", False,
                     id="passwords without uppercase letter"),
        pytest.param("qwertyR!", False, id="passwords without digits"),
        pytest.param("qW1!", False, id="short passwords"),
        pytest.param("qwertyR2", False,
                     id="passwords without special symbols"),
        pytest.param("qwertyR2ssrrr!dgrhasdfdgrhre", False,
                     id="too long passwords")
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result

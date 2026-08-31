import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("qWe@ty1", False, id="password short, need more symbols"),
        pytest.param("qwertyuiopasdfghj", False,
                     id="Password too long should be less symbols"),
        pytest.param("славаУкраїні@1", False,
                     id="Password should contain only latin lettes"),
        pytest.param("Geroyamslava1", False,
                     id="Password should contain at least 1 special symbol"),
        pytest.param("Pass@word1", True)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) is result

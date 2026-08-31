import pytest

from app.main import check_password


@pytest.mark.parametrize("password, result", [
    pytest.param("Pass@word1", True),
    pytest.param("qwerty", False),
    pytest.param("Str@ng", False),
    pytest.param("Pass@word", False),
    pytest.param("Pass@1", False),
    pytest.param("Password1", False),
    pytest.param("pass@word1", False),
    pytest.param("Pass@word1dfjsldfjlaskjdflsasdl", False)
])
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

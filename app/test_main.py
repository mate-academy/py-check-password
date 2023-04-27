import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "test_word, result_pass",
    [
        pytest.param("Pass@word1", True,
                     id="good password"),
        pytest.param("Pass@word", False,
                     id="checking for numbers"),
        pytest.param("Password1", False,
                     id="checking for special simbols '$@#&!-_'"),
        pytest.param("pass@word1", False,
                     id="checking for a capital letter"),
        pytest.param("Qwe&ty1", False,
                     id="check for password length (at least 8)"),
        pytest.param("Qwertyuiop12#asdf", False,
                     id="check for password length (no more than 16)")
    ]
)
def test_check_password_functional(test_word: str, result_pass: bool) -> None:
    assert check_password(test_word) == result_pass

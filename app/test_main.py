import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param("Pass@word1", True, id="Valid password"),
        pytest.param("Qwe@rty1", True, id="Exactly 8 symbols"),
        pytest.param("pass@word1", False, id="without upper case letters"),
        pytest.param("Pass@word", False, id="without digits"),
        pytest.param("Password1", False, id="without symbols"),
        pytest.param("Str@ng1", False, id="To short"),
        pytest.param("Pass@word1andsometext", False, id="To long"),
        pytest.param("Pass@word1_word2", True, id="Exactly 16 symbols"),
    ]
)
def test_check_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result

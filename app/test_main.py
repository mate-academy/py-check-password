import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("", False, id="empty password"),
        pytest.param("Pass@word1", True, id="valid password"),
        pytest.param("qwerty", False, id="only_lower_letters"),
        pytest.param("Pass@word", False, id="without_numbers"),
        pytest.param("Str@ng1", False, id="small_password"),
        pytest.param("123456789", False, id="only_numbers"),
        pytest.param("Pass@word1lkbjosgj", False, id="too_long_password"),
        pytest.param("Password1", False, id="without_special_symbols"),
        pytest.param("pass@word1", False, id="without_uppercase"),

    ])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

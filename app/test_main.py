# write your code here
from typing import Any

import pytest

from app.main import check_password


@pytest.mark.parametrize("password, expected_result", [
    ("Pass@word1", True),
    ("pass@word1", False),
    ("Password1", False),
    ("qwerty", False),
    ("Str@ng", False),
    ("Wr1@t", False),
    ("Pass@word1Pass@word1", False),
    ("Pass@wordPa", False),
])
def test_check_password(password: str,
                        expected_result: bool) -> None:
    assert expected_result == check_password(password)


@pytest.mark.parametrize("invalid_input", [
    10,
    None,
])
def test_get_type_error(invalid_input: Any) -> None:
    with pytest.raises(TypeError):
        check_password(invalid_input)

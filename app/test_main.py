from app.main import check_password

import pytest


@pytest.mark.parametrize("password, expected_result", [
    ("Pass1@", False),
    ("Password1@Password", False),
    ("password1@", False),
    ("Password@", False),
    ("Password1", False)])
def test_should_return_bool(password: str,
                            expected_result: bool) -> None:
    assert check_password(password) == expected_result

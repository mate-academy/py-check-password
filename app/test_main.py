import pytest

from app.main import check_password


@pytest.mark.parametrize("password,expected_tesult",
                         [
                             pytest.param("Pass@word1", True,
                                          id="Password is correct"),
                             pytest.param("Withoutspecial10", False,
                                          id="Password without special sign"),
                             pytest.param("Str@ng3", False,
                                          id="Password is sort"),
                             pytest.param("Passwords_", False,
                                          id="Password without digits"),
                             pytest.param("passswordac10#@!", False,
                                          id="Password without uppercase"),
                             pytest.param("Passwordwithmanycharacters10!",
                                          False,
                                          id="Password is long")
                         ]
                         )
def test_check_password(password, expected_tesult):
    assert check_password(password) == expected_tesult

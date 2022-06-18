import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected_output",
                         [
                             pytest.param("Pass@word1", True,
                                          id="password meets all conditions"),
                             pytest.param("Pa@wd1", False,
                                          id="password too short"),
                             pytest.param("pass@word1", False,
                                          id="password missing"
                                             " uppercase letter"),
                             pytest.param("Password1", False,
                                          id="password missing"
                                             " special character"),
                             pytest.param("Pass@word", False,
                                          id="password missing a digit"),
                             pytest.param("Pass@word1toolong", False,
                                          id="password too long"),
                         ])
def test_valid_password(password, expected_output):
    assert check_password(password) == expected_output

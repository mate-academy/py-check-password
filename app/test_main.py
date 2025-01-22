import pytest
from app.main import check_password


@pytest.mark.parametrize("current_password, expected_password",
                         [
                             pytest.param("Pass@word1",
                                          True,
                                          id="Password is valid"),
                             pytest.param("pass@word1",
                                          False,
                                          id="Password has"
                                             " not upper letter"),
                             pytest.param("Pass@word",
                                          False,
                                          id="Password has"
                                             " not digit letter"),
                             pytest.param("Password1",
                                          False,
                                          id="Password has"
                                             " not special sumbol"),
                             pytest.param("Pass@word1Password1P",
                                          False,
                                          id="Password is"
                                             " to long"),
                             pytest.param("Pass@1",
                                          False,
                                          id="Password is"
                                             " less 8 characters"),
                         ])
def test_check_password(current_password: str,
                        expected_password: bool) -> None:
    result = check_password(current_password)
    assert result == expected_password

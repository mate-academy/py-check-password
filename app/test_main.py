import pytest

from app.main import check_password


@pytest.mark.parametrize("tested_password,expected_result",
                         [
                             pytest.param("str123@iif", False,
                                          id="should not pass password "
                                             "only without uppercase later"),
                             pytest.param("Str@#nfgg", False,
                                          id="should not pass password "
                                             "without digit"),
                             pytest.param("Str145nfg", False,
                                          id="should not pass password "
                                             "without special character"),

                             pytest.param("P@s1rd4", False,
                                          id="should not pass password "
                                             "less than 8 characters"),
                             pytest.param("P@3s1rd4s1rd4e1ee", False,
                                          id="should not pass password "
                                             "more than 16 characters"),
                             pytest.param("P@s1rd4s1^rd4eee", False,
                                          id="should not pass with not "
                                             "allowed symbols"),
                             pytest.param("Pass@word1", True,
                                          id="should pass password"),

                         ])
def test_check_password(tested_password: str,
                        expected_result: bool) -> None:
    assert check_password(tested_password) == expected_result

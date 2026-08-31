import pytest

from app.main import check_password


@pytest.mark.parametrize("password,expected_result",
                         [
                             pytest.param("Pass@word1", True,
                                          id="\'Pass@word1\' "
                                             "is correct password"),

                             pytest.param("Pass@worФ1", False,
                                          id="\'Pass@worФ1\' "
                                             "contains non latin symbol"),

                             pytest.param("Pass@wor+1", False,
                                          id="\'Pass@wor+1\' "
                                             "contains non allowed"
                                             " symbol/'+/'"),

                             pytest.param("Pass@w1", False,
                                          id="\'Pass@w1\' "
                                             "contains less than 8 symbols"),

                             pytest.param("Pass@worqqqqqqqq1", False,
                                          id="\'Pass@worqqqqqqqq1\' "
                                             "contains more than 16 symbols"),

                             pytest.param("Passsword1", False,
                                          id="\'Passsword1\' "
                                             "contains no special symbols"),

                             pytest.param("pass@word1", False,
                                          id="\'pass@word1\' "
                                             "contains no upper case symbols"),

                             pytest.param("Pass@wordd", False,
                                          id="\'Pass@wordd\' "
                                             "contains no digits"),
                         ]

                         )
def test_check_password(password: str, expected_result: bool) -> None:
    assert expected_result == check_password(password)

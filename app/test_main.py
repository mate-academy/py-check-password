from app.main import check_password
import pytest


@pytest.mark.parametrize("password,expected",
                         [
                             pytest.param("Pass@word1",
                                          True,

                                          id="ok"),
                             pytest.param("qwerty111!ax",
                                          False,
                                          id="all lowercase"),
                             pytest.param("Stron!@#g",
                                          False,
                                          id="no digits"),
                             pytest.param("!2Km",
                                          False,
                                          id="too short"),
                             pytest.param("kakN1!tmzl3kasmlokskndualsjncuizhs",
                                          False,
                                          id="too long"),
                             pytest.param("K2kas3561",
                                          False,
                                          id="no special symbols")
                         ]
                         )
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

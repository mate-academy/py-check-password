import pytest

from app.main import check_password


@pytest.mark.parametrize("is_valid, result", [

                         pytest.param("Pass@word1", True,

                                      id="all requirements complete"),

                         pytest.param("Pass@word", False,

                                      id="has no digit"),

                         pytest.param("Pass@1", False,

                                      id="too short password"),

                         pytest.param("Paaaaaaaaaaass@word1", False,

                                      id="too long password"),

                         pytest.param("pass@word1", False,

                                      id="uppercase missed"),

                         pytest.param("Passaword1", False,

                                      id="without special")]

                         )
def test_is_valid_password(is_valid: callable, result: callable) -> None:

    assert check_password(is_valid) == result

import pytest
from app.main import check_password


@pytest.mark.parametrize("input_password,expected", [
    pytest.param("Pass@word1", True,
                 id="Should return True if password match "
                    "the requirements"),
    pytest.param("F1_oplk", False,
                 id="Should return False if password length "
                    "is less than 8 characters"),
    pytest.param("L7_kmju8iod_kmnbvs", False,
                 id="Should return False if password length "
                    "is greater than 16 characters"),
    pytest.param("1Ldslmdfe", False,
                 id="Should return False if password does not "
                    "1 special character"),
    pytest.param("_Ldsgfdre", False,
                 id="Should return False if password does not "
                    "have 1 digit"),
    pytest.param("19ds_lmdfe", False,
                 id="Should return False if password does not "
                    "have 1 uppercase letter"),
])
def test_check_password(input_password: str, expected: bool) -> None:
    assert check_password(input_password) == expected

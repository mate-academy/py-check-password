import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result", [
        pytest.param("Pass@word1", True),
        pytest.param("Pass@wo1", True),
        pytest.param("Pass@word555ewew", True),
        pytest.param("Password1", False, id="Missing special symbol"),
        pytest.param("Pass@ord", False, id="Missing number symbol"),
        pytest.param("@assword1", False, id="Missing uppercase symbol"),
        pytest.param("Pass@wo", False, id="Length password less 8 symbol"),
        pytest.param("Pass@word555ewews", False,
                     id="Length password more 16 symbol"),
        pytest.param("Pass word1", False, id="Whitespace in password"),
        pytest.param("", False, id="String with password is empty")
    ]
)
def test_check_password(password, result):
    assert check_password(password) == result

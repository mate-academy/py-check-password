import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param("Pas123!", False,
                     id="Shorter than 8"),
        pytest.param("This_Password", False,
                     id="'Must contain digits"),
        pytest.param("Pass123456", False,
                     id="Must contain special symbols"),
        pytest.param("123456!&^%$.", False,
                     id="Must contain letters"),
        pytest.param("Pass123456!_pass!_!", False,
                     id="Must be shorter than 16"),
        pytest.param("pass123456!_", False,
                     id="Must contain uppercase"),
        pytest.param("Pass123456!_", True,
                     id="Must be correct password"),
    ]
)
def test_should_return_proper_respond(password: str,
                                      expected_result: bool
                                      ) -> None:
    assert check_password(password) == expected_result

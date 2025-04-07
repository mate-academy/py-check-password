import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param("Pass@word",
                     False,
                     id="With no digits Test"),

        pytest.param("Pass@w1",
                     False,
                     id="Short password Test"),

        pytest.param("Password9",
                     False,
                     id="No special symbol Test"),

        pytest.param("password@1",
                     False,
                     id="No uppercase Test"),

        pytest.param("NotValid1234@Word!",
                     False, id="Too long password Test"),

    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

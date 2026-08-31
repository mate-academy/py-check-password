import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Pass@word1", True,
                     id="correct password"),
        pytest.param("Qwe@t1", False,
                     id="password to short"),
        pytest.param("Str@ngest", False,
                     id="password without digit"),
        pytest.param("Stronger1man", False,
                     id="password without special symbols"),
        pytest.param("password@1", False,
                     id="password without uppercase"),
        pytest.param("Param@word1ertfdgdt", False,
                     id="to long password")
    ]
)
def test_correct_password(
        password: str,
        result: bool,
) -> None:
    assert check_password(password) == result

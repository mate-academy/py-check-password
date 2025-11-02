import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("P@ssword1", True,
                     id="correct password"),
        pytest.param("Aa@1", False,
                     id="too short password"),
        pytest.param("A" * 14 + "a@1", False,
                     id="too long password"),
        pytest.param("p@ssword1", False,
                     id="password without uppercase letter"),
        pytest.param("Password1", False,
                     id="password without special symbol"),
        pytest.param("P@ssword", False,
                     id="password without number")
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected

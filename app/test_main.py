import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_result",
    [
        pytest.param("Pass@word1", True,
                     id="correct password is True"),
        pytest.param("Pass@word", False,
                     id="password without nums is False"),
        pytest.param("Password1", False,
                     id="password without spec.symbol is False"),
        pytest.param("Pa@wod1", False,
                     id="7-letters password is False"),
        pytest.param("Pass@word01234567", False,
                     id="17-letters password is False"),
        pytest.param("Ыass@word1", False,
                     id="Only latin letters available")
    ]
)
def test_check_password(password: str, is_result: bool) -> None:
    assert check_password(password) is is_result

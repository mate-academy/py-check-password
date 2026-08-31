import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param("J56&", False,
                     id="not enough chars"),
        pytest.param("J56&hdajhasdhgjahsgdjh", False,
                     id="too many chars"),
        pytest.param("t40@rere", False,
                     id="no upper letters"),
        pytest.param("Yt$UiUiU", False,
                     id="no digits"),
        pytest.param("567YtuYu", False,
                     id="no special symbols"),
        pytest.param("$HeyYou56", True,
                     id="correct input")
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

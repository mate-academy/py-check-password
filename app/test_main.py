import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("@Gbb3", False),
        pytest.param("asdFvfrtybfdsa56@", False),
        pytest.param("", False),
        pytest.param("fgrt3_gty", False),
        pytest.param("!_ghfDrhjuj", False),
        pytest.param("rthfLgbr34", False),
        pytest.param("Dsfgr43@vbn!", True),
    ],
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

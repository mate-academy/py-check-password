import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param(
            "Ala1@",
            False,
            id="should return False if password is short"
        ),
        pytest.param(
            "aSADLas@!",
            False,
            id="should return False if password doesn't have digits"
        ),
        pytest.param(
            "DASDdsaasd123",
            False,
            id="should return False if password doesn't have special symbols"
        ),
        pytest.param(
            "ASDASDASHFGUDS1H23IU1H47T47142618924@!#@#y!@HSAJIUDHASJKDHASKJD",
            False,
            id="should return False if password is too long"
        ),
        pytest.param(
            "asdasd123@!",
            False,
            id="should return False if password doesn't have uppercase letter"
        )

    ]
)
def test_check_password(
        password: str,
        expected: bool
) -> None:
    result = check_password(password)
    assert result == expected

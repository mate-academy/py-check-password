import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password_option, expected_result",
    [
        pytest.param("B1ba#dr", False, id="Too short password"),
        pytest.param("B1ba#drB1ba#dr111", False, id="Too long password"),
        pytest.param("Donny#diddd", False, id="No digit in password"),
        pytest.param("Donny1di", False, id="No special symbol entered"),
        pytest.param("1ba#1bad", False, id="No upper case letter entered"),
        pytest.param("B1ba#drB1", True, id="All requirements done"),
    ]
)
def test_check_password(
        password_option: str,
        expected_result: bool
) -> None:
    assert check_password(password_option) == expected_result

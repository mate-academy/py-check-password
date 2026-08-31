from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("Duckat4_Chip", True),
        pytest.param("D4_k", False),
        pytest.param("d_ckeatChupacab", False),
        pytest.param("Duckeat4Chip", False),
        pytest.param("u4ke_thip", False),
        pytest.param("uckeat4Chip", False),
        pytest.param("Duck_eat_4_Chipaa", False)

    ]
)
def test_check_password(password: str, expected: str) -> None:
    assert check_password(password) == expected

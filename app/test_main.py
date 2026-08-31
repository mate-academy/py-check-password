import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param("A1b$vfgT", True, id="all cases with min length"),
        pytest.param("A1b$vfg", False, id="length less 8"),
        pytest.param("A1b$vfgTA1b$vfgT", True, id="max length"),
        pytest.param("A1b$vfgTA1b$vfgT5", False, id="bigger than max length"),
        pytest.param("Ї1b$vfgTA1b$vfgT", False, id="not only latin alphabet"),
        pytest.param("a1b$vfgta1b$vfgt", False, id="no uppercase"),
        pytest.param("Aab$vfgTAab$vfgT", False, id="no digits"),
        pytest.param("A1bsvfgTA1bsvfgT", False, id="no special character")
    ]
)
def test_check_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result

from app.main import check_password
from typing import Any, Type
import pytest


@pytest.mark.parametrize(
    "tested_password,expected_result",
    [
        pytest.param(
            "Пароль0$", False, id="not Latin alphabet"
        ),
        pytest.param(
            "Anton__a", False, id="no digit"
        ),
        pytest.param(
            "Antona5+", False, id="special character not from list"
        ),
        pytest.param(
            "Anton343a", False, id="no special character"
        ),
        pytest.param(
            "Ant2_er", False, id="len 7"
        ),
        pytest.param(
            "Ant2_ere", True, id="len 8"
        ),
        pytest.param(
            "Antoooodsfdsgn2_", True, id="len 16"
        ),
        pytest.param(
            "Antoooodsfdss2_a1a", False, id="len 17"
        ),
    ]
)
def test_check_password(tested_password: str, expected_result: bool) -> None:
    assert check_password(tested_password) == expected_result


@pytest.mark.parametrize(
    "error_case,expected_error",
    [
        (
            123, TypeError
        )
    ]
)
def test_check_password_expected_error(
        error_case: Any,
        expected_error: Type[BaseException]
) -> None:
    with pytest.raises(expected_error):
        assert check_password(error_case)

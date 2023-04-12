import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "test_password,expected_result",
    [
        pytest.param(
            "aDjjdls45$",
            True
        ),
        pytest.param(
            "aDls45$",
            False
        ),
        pytest.param(
            "aDjjdls45$22241sdf",
            False
        ),
        pytest.param(
            "ajjdls45$",
            False
        ),
        pytest.param(
            "aDjjdls$",
            False
        ),
        pytest.param(
            "aDjjdls45",
            False
        )
    ]
)
def test_check_password(
        test_password: str,
        expected_result: bool
) -> None:
    assert check_password(test_password) == expected_result

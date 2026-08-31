import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result_of_checking",
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
def test_of_checking_password(
        password: str,
        result_of_checking: bool
) -> None:
    assert check_password(password) == result_of_checking

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,bool_value",
    [
        pytest.param(
            "skdjd!pojj",
            False,
        ),
        pytest.param(
            "Sfjk111@aaaaaaaaaaa",
            False
        ),
        pytest.param(
            "Sabs@sas",
            False
        ),
        pytest.param(
            "Las!34",
            False
        ),
        pytest.param(
            "9dhg@dlkhj",
            False
        )
    ]
)
def test_should_return_correct_bool_value(
    password: str,
    bool_value: bool
) -> None:
    assert check_password(password) == bool_value

import pytest


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param("dawdwaFdw&!", False, id="False if without numbers"),
        pytest.param(
            "123!4dwad5678",
            False,
            id="False if without uppercase"
        ),
        pytest.param(
            "1234dWad5678",
            False,
            id="False if without special symbols"
        ),
        pytest.param(
            "daw12dwaFdw&!",
            True,
            id="True if all conditions are met"
        ),
        pytest.param(
            "Fdhw&!dawdw1Fdw&!",
            False,
            id="False if too long"
        ),
        pytest.param(
            "D1w&!",
            False,
            id="False if too short"
        ),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    from app.main import check_password

    assert check_password(password) == expected

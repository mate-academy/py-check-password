import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "init_password, result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="Correct password"

        ),
        pytest.param(
            "Pass12@",
            False,
            id="Incorrect <8"
        ),
        pytest.param(
            "$ass12pAAASshfgt1",
            False,
            id="Incorrect >16"
        ),
        pytest.param(
            "Passwword1",
            False,
            id="Incorrect no special char"
        ),
        pytest.param(
            "pass$word1",
            False,
            id="Incorrect no upper char"
        ),
        pytest.param(
            "Pass$wordu",
            False,
            id="Incorrect no digit char"
        )
    ]
)
def test_all_check(init_password: str, result: bool) -> None:
    assert check_password(init_password) == result

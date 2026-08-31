from app.main import check_password

import pytest


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="check correct password"
        ),
        pytest.param(
            "Asdf5#lfnfhcljenc",
            False,
            id="check too long passwords"
        ),
        pytest.param(
            "Asdf5#j",
            False,
            id="check for short passwords and "
               "for passwords without special symbols"
        ),
        pytest.param(
            "fgnvh5#kf",
            False,
            id="check for passwords without uppercase letter"
        ),
        pytest.param(
            "Ghfnvk@fg",
            False,
            id="check for passwords without digits"
        ),

    ]
)
def test_check_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result

from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "checked_password, expected",
    [
        pytest.param(
            "paS@1", False,
            id="less than 8 characters"
        ),
        pytest.param(
            "Averyvery@Long5432ij", False,
            id="long password"
        ),
        pytest.param(
            "Pass@word1", True,
            id="password with letters, special symbols and numbers"
        ),
        pytest.param(
            "Qwerty123", False,
            id="without special symbol"
        ),
        pytest.param(
            "passwithou@1t", False,
            id="without uppercase"
        ),
        pytest.param(
            "Stro@ngpass", False,
            id="without digits"
        ),
    ]
)
def test_password(checked_password, expected):
    assert check_password(checked_password) == expected

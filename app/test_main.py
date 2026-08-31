import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "A2@bcdefgujk",
            True,
            id=">8 characters"
        ),
        pytest.param(
            "qQ#3ty",
            False,
            id="<8 characters"
        ),
        pytest.param(
            "Q#123wertyqwertqwertqweryqwertyqwetyqwety",
            False,
            id=">16 characters"
        ),
        pytest.param(
            "abcfedft123#ghq",
            False,
            id="no upercase character"
        ),
        pytest.param(
            "Z2bcfedftghq",
            False,
            id="no special character"
        ),
        pytest.param(
            "Z#bcfedftghq",
            False,
            id="no digit"
        )
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected

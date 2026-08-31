import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("SuperP@ss007", True),
        ("SuperHyperVeryP@ss007", False),
        ("P@ss007", False),
        ("P@ss()()/", False),
        ("superp@ss007", False),
        ("Superp@ss", False),
        ("SuperPass007", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

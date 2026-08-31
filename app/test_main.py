import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,correct",
    [
        ("aSdfasd3!", True),
        ("aSdfasd3", False),
        ("aSdfasd!", False),
        ("asdfasd3!", False),
        ("aSdfa2!", False),
        ("aSdasdffasdsasa2!", False)
    ],
    ids=(
        "Check correct password",
        "Check without special character",
        "Check without digit",
        "Check without uppercase letter",
        "Check small length",
        "Check big length",
    )
)
def test_check_password(password: str, correct: bool) -> None:
    assert check_password(password) is correct

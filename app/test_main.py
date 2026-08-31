import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        (
            "Pass@word1",
            True,
        ),
        (
            "Pass@word",
            False,
        ),
        (
            "Pass@worddfgsdfgdfgsafdsdf1",
            False,
        ),
        (
            "Pas@wf1",
            False,
        ),
        (
            "pass@word1",
            False,
        ),
    ]
)
def test_can_access_google_page(
        password: str,
        expected: bool
) -> None:

    assert check_password(password) == expected

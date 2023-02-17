import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Wr@7g", False),
        ("1werd!swxcvb", False),
        ("S1sdfssdfs", False),
        ("Str@ngasfdafasdfa1sdfas", False),
        ("tr#gasFdafasdfa", False),

    ]
)
def test_can_access_google_page(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result

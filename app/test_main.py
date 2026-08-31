import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("DinDj@rin20", True),
        ("Grogu", False),
        ("M@ndo", False),
        ("ThisIsTheWay@mando20", False),
        ("strWrs!mnd", False),
        ("", False),
        ("20MND!", False),
        ("Mandalorian20", False),
        ("mandalorian20!", False)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("u#G182", False),
        ("hasdhjlkhksretk85@xD", False),
        ("YTRsjplmsd#б", False),
        ("Qga318sahgdash", False),
        ("lhfnroPotus@", False),
        ("qwert1y@", False)
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result

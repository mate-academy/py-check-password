import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "incoming_password, expected_result",
    [
        ("QGe#VQjkgw", False),
        ("QGe#VQjkg241Ge#VQjkgw", False),
        ("QGe#214", False),
        ("qwertty@31g", False),
        ("qwerQty31g", False),
        ("ThisC0rr3ctP@ss", True)
    ]
)
def test_check_password(
        incoming_password: str,
        expected_result: bool
) -> None:
    assert check_password(incoming_password) == expected_result

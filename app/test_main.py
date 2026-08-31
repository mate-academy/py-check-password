import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("фкуфпакфум", False),
        ("v8U_L", False),
        ("cnjsrrjjyfaf", False),
        ("vh798U_!LHLvh798U_!LHLvh798U_!LHL", False),
        ("visjb1jsljk", False),
        ("vuvvBO776LUYGB", False),
        ("vuvvBL_UYGB", False),
        ("vuvv_____1", False),
        (",./,./,d./,./", False),
        ("vh798U_!LHL", True),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

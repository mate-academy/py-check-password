import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("Ss1@s", False),
        ("Aldj1lsk&jlkjdaadf____", False),
        ("asdd@12212", False),
        ("sddfsfsdffff", False),
        ("Msds1asd&_", True),
        ("Asdsdf$sdf", False),
        ("1123123123", False),
        ("adsWasdasd1", False),
        ("&%$%&&^*$%^", False)
    ]
)
def test_check_password(password: str,
                        expected_result: bool) -> None:

    assert check_password(password) == expected_result

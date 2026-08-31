import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "enter_data,result",
    [
        ("1!Aqwqer", True),
        ("aagdaaaaaaA#", False),
        ("a!2Afsfsfsffsfsdfsfs", False),
        ("=+fdsfs", False),
        ("aagdaaaaaa2#", False),
        ("aagdaaaaaa2A", False),
        ("1aA!", False),
    ]
)
def test_check_password(
        enter_data: str,
        result: bool
) -> None:
    assert check_password(enter_data) == result

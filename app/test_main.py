import pytest
from app.main import check_password


@pytest.mark.parametrize("test_password, expected_result", [
                         ("WithKirical0@Ж", False),
                         ("Les@8", False),
                         ("Biggerthen16@a8ajYfhj@", False),
                         ("Withounumm@", False),
                         ("Without1Spec", False),
                         ("df4zthr@a", False),
                         ("AHFYGK132@a", True),
                         ("РПВРрывыврп@67", False),
                         ])
def test_check_password(test_password: str, expected_result: bool) -> None:
    assert check_password(test_password) == expected_result

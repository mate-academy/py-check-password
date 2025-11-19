import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("ahsa2!aucde", False),  # no uppercase letter
        ("ahsSA!axXcc", False),  # no digit
        ("ahsSA4axXcc", False),  # no special character
        ("aHsS2!a", False),  # < 8 len
        ("ahsS2!axXcc14!fhSC", False),  # > 16 len
        ("ahsS2!axXcc!33kC", True),  # = 16 len
        ("ahsS2!axXcc", True),  # = 8 len
        ("aHsS2!aX", True)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

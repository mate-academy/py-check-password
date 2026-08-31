import pytest

from app.main import check_password


@pytest.mark.parametrize("variant_of_pass", [
    "pos$yd0n",
    "Qwe@ty1",
    "Posseydon_26081987",
    "Struhanets2608",
    "Struhan@t$"
])
def test_when_pass_must_been_not_correct(variant_of_pass: str) -> None:
    assert not check_password(variant_of_pass)

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("As1@gbB", False),
        ("S1t1r@2ngVewCs214", False),
        ("Str1ngFor", False),
        ("Str@nnj!g", False),
        ("trs3!1@ng", False),
        ("SigK2@!J", True),
        ("b09dV!fStr@nfV4g", True),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    func_result = check_password(password)

    assert func_result == result

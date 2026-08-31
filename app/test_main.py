import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Pass@word1", True, id="one test"),
        pytest.param("Vass@word1fffffffff", False, id="very long"),
        pytest.param("V2@f", False, id="very short"),
        pytest.param("Str@ngahk", False, id="not numbers"),
        pytest.param("S2fbfbfbf", False, id="not special symbols"),
        pytest.param("@2fbfbfaf", False, id="not uppercase letter"),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    res = check_password(password)
    assert res == result

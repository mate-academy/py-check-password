import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "incoming,expected",
    [
        pytest.param("Pass@word1", True, id=""),
        pytest.param("pass@word1", False, id=""),
        pytest.param("Passsword1", False, id=""),
        pytest.param("Pass@wordd", False, id=""),
        pytest.param("P@word1", False, id=""),
        pytest.param("Pass@word1aaaaaaaaaaaaaaaaaa", False, id="")
    ]
)
def test_can_sum(incoming: str, expected: bool) -> None:
    assert (
        check_password(incoming) == expected
    ), f"Result '{check_password(incoming)}' should be equal to '{expected}'"

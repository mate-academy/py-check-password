import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "checked_password, expected_result",
    [
        pytest.param("A@asdfghj1", True, id="all requirements used"),
        pytest.param("A@a1", False, id="short password"),
        pytest.param("A@asdfghj1klzxcvb", False, id="long password"),
        pytest.param("A@asdfghj", False, id="hasn't digit"),
        pytest.param("Aasdfghj1", False, id="hasn't special symbol"),
        pytest.param("a@asdfghj1", False, id="hasn't upper case"),
    ]
)
def test_check_password(
        checked_password: str,
        expected_result: bool
) -> None:
    assert check_password(checked_password) == expected_result

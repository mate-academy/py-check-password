import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "checked_password, expected_result",
    [
        pytest.param("A@asdfghj1", True, id="All requirements used"),
        pytest.param("A@a1", False, id="Password is too short"),
        pytest.param("A@asdfghj1klzxcvb", False, id="Password is too long"),
        pytest.param("A@asdfghj", False, id="1 digit required"),
        pytest.param("Aasdfghj1", False, id="1 special symbol required"),
        pytest.param("a@asdfghj1", False, id="1 upper case required"),
    ]
)
def test_check_password(
        checked_password: str,
        expected_result: bool
) -> None:
    assert check_password(checked_password) == expected_result

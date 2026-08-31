import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "initial_password, expected_result",
    [
        pytest.param("Pass@word", False),
        pytest.param("Sh@or1", False),
        pytest.param("with@utup1", False),
        pytest.param("Thisisveryl@ngpassword1", False),
        pytest.param("Pass@word1", True),
    ],
    ids=[
        "Invalid password without digit",
        "Invalid too short password",
        "Invalid password without uppercase letter",
        "Invalid too long password",
        "Valid password",
    ]
)
def test_check_password(initial_password: str,
                        expected_result: bool) -> None:
    assert check_password(initial_password) == expected_result

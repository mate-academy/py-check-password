import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param(
            "C0d_123",
            False,
            id="Password is too short"
        ),
        pytest.param(
            "C0d_codede1234567",
            False,
            id="Password is too long"
        ),
        pytest.param(
            "C0d_codede123456",
            True,
            id="Valid password"
        ),
        pytest.param(
            "c0d_1234",
            False,
            id="Should have upper case characters"
        ),
        pytest.param(
            "Cod_Cod_",
            False,
            id="Should have digits"
        ),
        pytest.param(
            "C0de1234",
            False,
            id="Should have special"
        ),
        pytest.param(
            "C0d_1234",
            True,
            id="Valid password"
        )
    ]
)
def test_password_correctness(
    password: str,
    expected_result: bool
) -> None:
    assert check_password(password) == expected_result

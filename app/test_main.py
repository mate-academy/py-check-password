import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_value",
    [
        pytest.param(
            "A@ze2", False,
            id="check too short password"
        ),

        pytest.param(
            "Aazerdsgdfgdfsf_dhfsfg12sf", False,
            id="check too long password"
        ),

        pytest.param(
            "Password_@$", False,
            id="check without digit"
        ),

        pytest.param(
            "password_12", False,
            id="check without uppercase letter"
        ),

        pytest.param(
            "Password112", False,
            id="check without special character"
        ),

        pytest.param(
            "Password_@112", True,
            id="check valid"
        ),
    ]
)
def test_check_password(password: str, expected_value: bool) -> None:
    assert check_password(password) == expected_value

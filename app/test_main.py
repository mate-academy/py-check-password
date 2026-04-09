import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password, valid",
    [
        pytest.param(
            "Pass@word1", True,
            id="check valid password"
        ),
        pytest.param(
            "qwerty", False,
            id="check password of only letters"
        ),
        pytest.param(
            "Str@ngpassword", False,
            id="check password of no numbers"
        ),
        pytest.param(
            "Str0ngpas", False,
            id="check password of no special characters"
        ),
        pytest.param(
            "pass@word1", False,
            id="check password of no uppercase letters"
        ),
        pytest.param(
            "Pass@1", False,
            id="check password too short"
        ),
        pytest.param(
            "Pass@1word1word1word1word1word1word1", False,
            id="check password too long"
        ),
    ]
)
def test_check_password(password: str, valid: bool) -> None:
    assert check_password(password) == valid

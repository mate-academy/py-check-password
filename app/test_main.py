import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param(
            "",
            False,
            id="empty string"
        ),
        pytest.param(
            "укрпвлм123",
            False,
            id="non-english chars"
        ),
        pytest.param(
            "Super1@",
            False,
            id="under 8 chars"
        ),
        pytest.param(
            "superpassword1@",
            False,
            id="without uppercase letters"
        ),
        pytest.param(
            "Qwerty1234",
            False,
            id="without special char"
        ),
        pytest.param(
            "Nodigits$",
            False,
            id="without digits"
        ),
        pytest.param(
            "SupperLooooong1@",
            True,
            id="16 chars"
        ),
        pytest.param(
            "SupperLoooo0ng1@#",
            False,
            id="<16 chars"
        ),
        pytest.param(
            "Vvalid1#",
            True,
            id="8 chars"
        ),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

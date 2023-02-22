import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, expected",
        [
            pytest.param(
                "Pas@1", False,
                id="too short"
            ),
            pytest.param(
                "Pas@1Pas@1Pas@1Pas@1Pas@1Pas@1Pas@1Pas@1Pas@1", False,
                id="too long"
            ),
            pytest.param(
                "@$#&!-_12345678", False,
                id="no upper"
            ),
            pytest.param(
                "Passwo@rd1", True,
                id="valid"
            ),
            pytest.param(
                "фійцувати", False,
                id="cyrillic"
            ),
            pytest.param(
                "Password1", False,
                id="no special"
            ),
            pytest.param(
                "Password@", False,
                id="no digit"
            )
        ]
    )
    def test_check_password(self, password: str, expected: bool) -> None:
        assert check_password(password) == expected

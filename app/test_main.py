from app.main import check_password
import pytest


class TestModify:
    @pytest.mark.parametrize(
        "password, result",
        [
            pytest.param(
                "Pass@word1",
                True,
                id="Test#1"
            ),
            pytest.param(
                "qwerty",
                False,
                id="Test#2"
            ),
            pytest.param(
                "qWrty1@",
                False,
                id="Test#2"
            ),
            pytest.param(
                "qw123rty1@",
                False,
                id="Test#2"
            ),
            pytest.param(
                "qWrty1@asdasdasdsadadsada",
                False,
                id="Test#2"
            ),
            pytest.param(
                "",
                False,
                id="Test#2"
            ),
            pytest.param(
                "qwert@Qqqy",
                False,
                id="Test#2"
            ),
            pytest.param(
                "qwert1Qqqy",
                False,
                id="Test#2"
            ),
            pytest.param(
                "q",
                False,
                id="Test#2"
            ),
            pytest.param(
                "Str@ng",
                False,
                id="Test#3"
            ),
        ]
    )
    def test_modify(self, password: str, result: bool) -> None:
        assert check_password(password) == result

import pytest
from app.main import check_password


class TestPassword():
    @pytest.mark.parametrize(
        "test_pwd,bool_result",
        [
            ["Pass@word1", True],
            ["qwerty", False],
            ["Str@ng", False],
            ["Pass@word1111111111", False],
            ["P@o1", False],
            ["Password1", False],
            ["ppp@111fresh", False],
            ["Banana@milk", False]
        ]
    )
    def test_check_password(
            self,
            test_pwd: str,
            bool_result: bool
    ) -> None:
        assert check_password(test_pwd) == bool_result

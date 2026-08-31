import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "initial_value,result",
        [
            pytest.param(
                "Ght1@",
                False,
                id="returns False for short passwords"
            ),
            pytest.param(
                "Srgsrgrsgrgrgdrsgdrgr@1",
                False,
                id=" returns False for too long passwords"
            ),
            pytest.param(
                "justcheck@1",
                False,
                id="returns False for passwords without uppercase letter"
            ),
            pytest.param(
                "Justckeck@",
                False,
                id="returns False for passwords without digits"
            ),
            pytest.param(
                "CheckIsEasy1111",
                False,
                id="returns False for passwords without special symbols"
            ),
            pytest.param(
                "Pass@word1",
                True,
                id="ok"
            ),
        ]
    )
    def test_check_password(
            self,
            initial_value: object,
            result: bool
    ) -> None:
        assert check_password(initial_value) is result

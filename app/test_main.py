from app.main import check_password
import pytest


class Test:
    @pytest.mark.parametrize(
        "password, result",
        [
            ("qE@pzm2", False),
            ("iamtoolong4te$ts!A", False),
            ("iamnothaveup$rs1", False),
            ("iamnoth@Vedigit", False),
            ("iamnothavEspec2", False),
        ]
    )
    def test_check_password(self, password, result):
        assert check_password(password) == result

import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password,result",
        [
            ("Mate@academy1", True),
            ("Mateacademy1", False),
            ("mate", False),
            ("Mate@academy", False),
            ("mate@academy1", False),
            ("111222@222111", False),
            ("", False),
            ("Mate@1", False),
            ("Mate@academyNumber1ever", False)

        ]
    )
    def test_valid_password(self, password, result):
        assert check_password(password) is result

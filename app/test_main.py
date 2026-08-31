import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "key, value",
        [
            ("Pass@word1", True),
            ("Password!!!", False),
            ("Password123", False),
            ("Passw@rd_1s_to_long", False),
            ("passw@rd1", False),
            ("P@s1", False)
        ]
    )
    def test_check_password(self, key: str, value: bool):
        assert check_password(key) == value

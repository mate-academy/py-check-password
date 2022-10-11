import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "test_password, expected_result",
        [
            ("Very_long_password12$@#", False),
            ("Short1$", False),
            ("with0utChar", False),
            ("with0ut_upper!", False),
            ("withOut_giG@", False),
            ("Pass@word1", True)
        ]
    )
    def test_check_password(
            self,
            test_password: str,
            expected_result: bool
    ) -> None:
        assert check_password(test_password) == expected_result

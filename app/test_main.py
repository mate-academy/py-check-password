import pytest

from app.main import check_password


class TestPassword:
    @pytest.mark.parametrize(
        "password, expected_result",
        [
            ("Pass@word1", True),
            ("Pass@11", False),
            ("Pass@word1qqqqqqq", False),
            ("Password11", False),
            ("Password@@", False),
            ("pass@word1", False)
        ]
    )
    def test_password(
            self,
            password: str,
            expected_result: bool
    ) -> None:
        assert check_password(password) == expected_result

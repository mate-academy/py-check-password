import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password,expected_result",
        [
            pytest.param(
                "Pass@wordd",
                False
            ),
            pytest.param(
                "Passwword1",
                False
            ),
            pytest.param(
                "pass@word1",
                False
            ),
            pytest.param(
                "Q@1rtyuiopasdfghj",
                False
            ),
            pytest.param(
                "Q@1rtyu",
                False
            ),
            pytest.param(
                "Pass@word1",
                True
            ),
        ]
    )
    def test_check_password_return_correct_bool(
            self,
            password: str,
            expected_result: bool
    ) -> None:
        assert check_password(password) == expected_result

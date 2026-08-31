import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password,expected_result",
        [
            pytest.param(
                "Кітпес123!",
                False,
                id="work with latina alphabet"
            ),
            pytest.param(
                "minimum1upper1!",
                False,
                id="should consists at least 1 upper"
            ),
            pytest.param(
                "Minimumonedigit!",
                False,
                id="should consists at least 1 digit"
            ),
            pytest.param(
                "MinimumonesymboL1",
                False,
                id="should consists at least one symbol: $@#&!-_"
            ),
            pytest.param(
                "Min!ee1",
                False,
                id="at least 8 characters"
            ),
            pytest.param(
                "Maximumlength1!123",
                False,
                id="maximum 16 characters inclusive"
            ),
            pytest.param(
                "Pass@word1",
                True,
                id="1 upper/digit/symbol, good length, using latina alphabet"
            )
        ]
    )
    def test_check_password(
            self,
            password: str,
            expected_result: bool
    ) -> None:
        assert check_password(password) == expected_result

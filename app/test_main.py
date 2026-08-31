import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password,boolean",
        [
            pytest.param("Pass@word", False, id="should be digets symbols"),
            pytest.param(
                "qwert-y5kr",
                False,
                id="should be upper and special symbols"),
            pytest.param("Q@2erty", False, id="must be at least 8 symbols"),
            pytest.param(
                "dcNdajsKcn3@sdkcnbb",
                False,
                id="must be maximum 16 characters"),
            # pytest.param()

        ]
    )
    def test_oll_symbols_is_in_password(
        self,
        password: str,
        boolean: bool
    ) -> None:
        assert check_password(password) == boolean

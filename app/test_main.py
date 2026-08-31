import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, result",
        [
            pytest.param(
                "Мn!1",
                False,
                id="Should return False"
            ),
            pytest.param(
                "Попробуем_this",
                False,
                id="not all letters are in English"
            ),
            pytest.param(
                "Password1",
                False,
                id="without special characters"
            ),
            pytest.param(
                "passwor1d_",
                False,
                id="without capital letter"
            ),
            pytest.param(
                "My_password1",
                True,
                id="should return True"
            ),
            pytest.param(
                "My_password1isverylongbatitisgoodsfdre",
                False,
                id="should return True"
            ),
            pytest.param(
                "Qwertyu!iop1asdf",
                True,
                id="should return False ven 16 symbol only"
            )
        ]
    )
    def test_check_password(self, password: str, result: bool) -> None:
        assert check_password(password) == result

import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password", [
            pytest.param("j@T9ku_a$-m#Ex&b", id="16 characters"),
            pytest.param("j@T9ku_!", id="8 characters"),
            pytest.param("ju@T9ku!!", id="repeated characters")
        ]
    )
    def test_correct_password(self, password: str) -> None:
        assert check_password(password) is True

    @pytest.mark.parametrize(
        "password", [
            pytest.param("", id="empty string"),
            pytest.param("j@T9ku!", id="too short"),
            pytest.param("j@T9ku_a$Rm#Ex&bp", id="too long"),
            pytest.param("jTkuamExb3", id="no special characters"),
            pytest.param("j@9ku_a$m#x8bp", id="no huge letters"),
            pytest.param("@R_$#BU-!", id="no small letters"),
            pytest.param("j@Rku_a$m#xBbp", id="no digits"),
            pytest.param("j<T9ku_am,Ex1b", id="not accepted characters")
        ]
    )
    def test_incorrect_password_empty(self, password: str) -> None:
        assert check_password(password) is False

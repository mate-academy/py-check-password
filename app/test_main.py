import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, expected_result",
        [
            pytest.param("Qwert1@", False, id="Password is too short"),
            pytest.param(
                "qwertYuio1pas@dfghjk", False, id="Password is too long"
            ),
            pytest.param(
                "qwertyu1@",
                False,
                id="Password should have at least 1 uppercase letter",
            ),
            pytest.param(
                "Qwertyu@", False, id="Password should have at least 1 digit"
            ),
            pytest.param(
                "Qwerty12",
                False,
                id="Password should have at least 1 special symbol",
            ),
            pytest.param(
                "1@Щосьукраїнською",
                False,
                id="Password should contain only Latin alphabet",
            ),
            pytest.param("Qwerty1@", True, id="Password is correct"),
        ],
    )
    def test_check_password(
        self, password: str, expected_result: bool
    ) -> None:
        assert expected_result == check_password(password)

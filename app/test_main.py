import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, result",
        [
            pytest.param("pass@word1", False, id="should return False"),
            pytest.param("Pass@word", False, id="should return False"),
            pytest.param("Pass@1", False, id="should return False"),
            pytest.param("Password1", False, id="should return False"),
            pytest.param("Pass@word1adsfsfg", False, id="should return False"),
            pytest.param("Pass@word1", True, id="should return True"),
        ],
    )
    def test_utmost_cases(self, password: str, result: bool) -> None:
        assert check_password(password) == result

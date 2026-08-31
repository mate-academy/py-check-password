import pytest

from app.main import check_password


class TestCheckPassword:

    @pytest.mark.parametrize(
        "input_password, is_correct",
        [
            pytest.param(
                "Hell@1",
                False,
                id="should return False when password is too short"
            ),
            pytest.param(
                "Passw@rdPassw@rdPassw@rdPassw@rd5",
                False,
                id="should return False when password is too long"
            ),
            pytest.param(
                "Passw@rd",
                False,
                id="should return False when there are no digits"
            ),
            pytest.param(
                "Passw0rd",
                False,
                id="should return False when there are no special characters"
            ),
            pytest.param(
                "_assw0rd",
                False,
                id="should return False when there are no uppercase letter"
            )
        ]
    )
    def test_returns_correct_answer(self, input_password, is_correct):
        assert check_password(input_password) == is_correct

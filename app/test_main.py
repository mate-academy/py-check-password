import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "input_password, result",
    [
        pytest.param(
            'Pass@word1', True,
            id="test when True"),
        pytest.param(
            'Qwer@1', False,
            id="test when not in range 8-16"),
        pytest.param(
            'str@ng111', False,
            id="test when one case is False"),
        pytest.param(
            'P@ssword_true1fal', False,
            id="test when too long password is False"),
        pytest.param(
            'strong111', False,
            id="test when no one special symbol"),
        pytest.param(
            'Strong_strongfff', False,
            id="test when no one digit")
    ]
)
def test_check_password(input_password, result):
    assert check_password(input_password) == result

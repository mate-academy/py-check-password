import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Passw@rd1", True, id="Test correct password"),
        pytest.param("qwerty1@", False, id="Test without uppercase letter"),
        pytest.param("Str@ng",
                     False,
                     id="Test short password when other rules correct"),
        pytest.param("Passw@rdStr0ngV3ry",
                     False,
                     id="Test long password when other rules correct"),
        pytest.param("Пар@ль12", False, id="Test if text in Cyrillic"),
        pytest.param("P@@$s'!d", False, id="Test if many special characters")
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

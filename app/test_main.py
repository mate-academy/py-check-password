import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param("Pass@word1", True,
                     id="correct password with letter, "
                        "number and special character"),
        pytest.param("Pass@word", False,
                     id="wrong password without number"),
        pytest.param("qwerty", False,
                     id="wrong password not enough characters, only letter"),
        pytest.param("qwerty@1", False,
                     id="wrong password without uppercase letter"),
        pytest.param("Str@ng", False,
                     id="wrong password not enough characters, "
                        "without numbers"),
        pytest.param("Str@ng12", True,
                     id="correct password good length 8 and characters"),
        pytest.param("Str@ng1", False,
                     id="wrong password length 7 not 8"),
        pytest.param("Str@ng12Pass@wor", True,
                     id="correct password good length 16 and characters"),
        pytest.param("Str@ng12Pass@wor1", False,
                     id="wrong password length 17 not 16"),
        pytest.param("Str @ng12", False,
                     id="wrong password consist wrong characters"),
        pytest.param("Str*@ng12", False,
                     id="wrong password consist wrong characters ***"),
        pytest.param("", False, id="empty string"),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result

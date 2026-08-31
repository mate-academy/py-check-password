import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, is_valid",
    [
        pytest.param("Pass@word1", True, id="Valid password"),
        pytest.param("Пароль23_", False,
                     id="Password must be of Latin alphabet"),
        pytest.param("Str@ng1", False,
                     id="Password must be at least "
                        "8 characters long"),
        pytest.param("fhdjHhcnfhr647fjr__", False,
                     id="Password should be less than "
                        "16 characters long"),
        pytest.param("qwerty", False,
                     id="Password must be at least 8 characters"
                        " long and contain at least 1 upper "
                        "letter, 1 special character and 1 digit"),
        pytest.param("qwerty12", False,
                     id="Password must contain at least 1 "
                        "upper letter and special character"),
        pytest.param("jdhfkjdhf___", False,
                     id="Password must contain at least 1 upper "
                        "letter and 1 digit"),
        pytest.param("Strongggggg", False,
                     id="Password must contain at least "
                        "1 digit and 1 special character"),
        pytest.param("Str@nggg", False,
                     id="Password must have at least one digit"),
        pytest.param("QWErty1234", False,
                     id="Password must contain at least "
                        "1 special character"),
        pytest.param("qwerty___123", False,
                     id="Password must contain at least 1 upper letter")
    ]
)
def test_all_possible_valid_and_invalid_passwords(
        password: str,
        is_valid: bool
) -> None:
    assert check_password(password) == is_valid

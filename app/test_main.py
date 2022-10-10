import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param(
            "Asd123$@", True
        ),
        pytest.param(
            "Asd123$@#Asd123$", True
        ),
        pytest.param(
            "Asd123$", False
        ),
        pytest.param(
            "Asd123$@#Asd123$@#", False
        ),
        pytest.param(
            "Asdbnm$@#", False
        ),
        pytest.param(
            "Qwerty123", False
        ),
        pytest.param(
            "qwerty&123", False
        ),
    ]

)
def test_check_password(password: str, expected: bool):
    assert check_password(password) is expected

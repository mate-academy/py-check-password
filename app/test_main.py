import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_bool",
    [
        ("Rwe8ke!", False),
        ("rwe$ikEe4rff23r45", False),
        ("dsf8sdf@fff", False),
        ("dsTsdf!ffe", False),
        ("d8sfsdfRffy", False),
    ]
)
def test_check_password(password, expected_bool):
    assert check_password(password) == expected_bool

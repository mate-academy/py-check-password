import pytest as pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param("7Lette_", False,
                     id="should return False if 7-letter password"),
        pytest.param("8Letter_", True,
                     id="should return True if 8-letter password"),
        pytest.param("16Letter_passwor", True,
                     id="should return True if 16-letter password"),
        pytest.param("17Letter_password", False,
                     id="should return False if 17-letter password"),
        pytest.param("No_numbers", False,
                     id="should return False if password has no numbers"),
        pytest.param("no_upper!3", False,
                     id="should return False if password has no uppercase"),
        pytest.param(
            "NoSpecial69",
            False,
            id="should return False if password has no special symbols"
        )

    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

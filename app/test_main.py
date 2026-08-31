import app.main
import pytest


@pytest.mark.parametrize(
    "input_password,expected_result",
    [
        pytest.param(
            "Qwey1!",
            False,
            id="should return False when len < 8"
        ),
        pytest.param(
            "IloveMAteAcademyNoHomo",
            False,
            id="should return False when len > 16"
        ),
        pytest.param(
            "ilovecoding!78",
            False,
            id="should return False when upper char is missed"
        ),
        pytest.param(
            "ILOVEMATEACADEMY1!",
            False,
            id="should return False when lower char is missed"),
        pytest.param(
            "Nothing+$%^*/\\",
            False,
            id="should return False with restricted symbols"
        ),
        pytest.param(
            "HelloWorld!",
            False,
            id="should return False if number is missed"
        ),
        pytest.param(
            "HelloWorld1",
            False,
            id="should return False if special char is missed"
        ),
        pytest.param(
            "HelloWorld1!",
            True,
            id="should return True"
        ),

    ]
)
def test_check_password(
        input_password: str,
        expected_result: bool

) -> None:
    assert app.main.check_password(input_password) == expected_result

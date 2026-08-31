import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("weackp@assword1", False),
        ("weacKpassword1", False),
        ("@aSswo1", False),
        ("Wvfvfvfeackp@ass1", False),
        ("weaCkp@assword", False),
        ("Weаckp@assword1", False)
    ],
    ids=[
        "At least must contain 1 uppercase letter",
        "At least must contain 1 special character",
        "The minimum password length must be 8 characters",
        "The maximum password length must be 16 characters",
        "Must contain at least 1 digit",
        "Accepts only letters of the Latin alphabet Aa-Zz"
    ]
)
def test_invalid_password(password: str, result: bool) -> None:

    assert (
        check_password(password) == result
    ), "The test result must be False"


@pytest.mark.parametrize(
    "password,result",
    [
        ("Passw0r!", True),
        ("veryL0ngP@ssword", True)
    ],
    ids=[]
)
def test_valid_password(password: str, result: bool) -> None:

    assert (
        check_password(password) == result
    ), "The test result must be True"

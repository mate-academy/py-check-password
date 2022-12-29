import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Asdwerdfа", False),
        ("A1@ghwdsrtysbvdfs", False),
        ("A1@ghb", False),

    ]

)
def test_password(password: str, result: bool) -> None:
    assert check_password(password) == result

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password",
    (
        "Pass@word12345xyz",
        "he3low@rld",
        "B0gd$n",
        "__qwErTy__",
        "ilovePython3000"
    )
)
def test_check_password(password: str) -> None:
    assert not check_password(password)

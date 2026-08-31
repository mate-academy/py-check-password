import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("1234", False, id="only numbers"),
        pytest.param("loijug", False, id="no digits"),
        pytest.param("loiju123g", False, id="without special symbols"),
        pytest.param("qdjbyugu121dferfr2QQ!!!!", False, id="too long"),
        pytest.param("1", False, id="min_length"),
        pytest.param("aoAdvtf1@", True, id="correct"),
        pytest.param("Jfnouyu19@", True, id="correct"),
        pytest.param("short", False, id="too short"),
        pytest.param("noppercase1!", False, id="no uppercase letters"),
        pytest.param("8рш1_шкЦИ", False, id="no special_symbols"),
    ]
)
def test_password(password: str, result: bool) -> None:
    assert check_password(password) == result

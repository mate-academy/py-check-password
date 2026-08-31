import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, value",
    [
        pytest.param(
            "12D4567$",
            True,
            id="correctly password"
        ),
        pytest.param(
            "1254G$iiiiiiiiggggggjjjjjjdftryryryiuio",
            False,
            id="very long password"
        ),
        pytest.param(
            "1254G$4",
            False,
            id="very short password"
        ),
        pytest.param(
            "12D4567u",
            False,
            id="without special symbol"
        ),
        pytest.param(
            "1254567u$",
            False,
            id="without upper case"
        ),
        pytest.param(
            "ghgDgjgjg$fjfjf",
            False,
            id="without digital"
        )
    ]
)
def test_correctly_password(password, value):
    assert check_password(password) == value

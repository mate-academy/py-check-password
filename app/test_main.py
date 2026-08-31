import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "test_password, result",
    [
        pytest.param(
            "@1Aa" + "0" * 3,
            False,
            id="Should False if len(password) < 8"
        ),
        pytest.param(
            "@1Aa" + "0" * 13,
            False,
            id="Should False if len(password) > 16"
        ),
        pytest.param(
            "@Aa" * 3,
            False,
            id="Should False if without digits"
        ),
        pytest.param(
            "AA" * 3,
            False,
            id="Should False if only uppercase"
        ),
        pytest.param(
            "@1aa" * 3,
            False,
            id="Should False if without uppercase"
        ),
        pytest.param(
            "1Aa" * 3,
            False,
            id="Should False if without special symbols"
        ),
    ]
)
def test_check_password_if_len_less_than_8(test_password, result):
    assert check_password(test_password) == result

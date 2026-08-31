import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param(
            "AAAbbb11@@_ЖЖЖ",
            False,
            id="Should only accept letters of the Latin alphabet"
        ),
        pytest.param(
            "AAAbbb11@@_???",
            False,
            id="Should accept only special characters from '$@#&!-_'"
        ),
        pytest.param(
            "Ab1@",
            False,
            id="Should be at least 8 characters"
        ),
        pytest.param(
            "AAAbbbCCC11@@__!!!!!",
            False,
            id="Should be maximum 16 characters inclusive"
        ),
        pytest.param(
            "AAAbbb11",
            False,
            id="Should contain at least 1 special character"
        ),
        pytest.param(
            "AAAbbb@@",
            False,
            id="Should contain at least 1 digit"
        ),
        pytest.param(
            "aaabbb11@@",
            False,
            id="Should contains at least 1 uppercase letter"
        ),
        ("AAAbbb11@@_", True),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

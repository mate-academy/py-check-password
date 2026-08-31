import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("qwerty1@", False),
        ("123456a#", False)

    ]
)
def test_is_pass_have_upper(password: str, result: bool) -> None:
    assert (
        check_password(password) == result
    ), f"{password} Should consist at least 1 upper letter"


@pytest.mark.parametrize(
    "password, result",
    [
        ("qwErty12", False),
        ("123456uD", False)

    ]
)
def test_is_pass_have_spec_ch(password: str, result: bool) -> None:
    assert (
        check_password(password) == result
    ), f"{password} Should consist at least 1 special character from ($@#&!-_)"


@pytest.mark.parametrize(
    "password, result",
    [
        ("asdFghJ@&&&", False),
        ("DRATUTI_rsn-pzd", False)

    ]
)
def test_is_pass_have_digits(password: str, result: bool) -> None:
    assert (
        check_password(password) == result
    ), f"{password} Should consist at least 1 digit"


@pytest.mark.parametrize(
    "password, result",
    [
        ("12345A@", False),
        ("ABCabc123@#$rathk", False),
        ("QWERTqwert178##@", True)

    ]
)
def test_is_pass_more_8_and_less_16(password: str, result: bool) -> None:
    assert (
        check_password(password) == result
    ), f"{password} Should be > 8 and < 16"

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "input_password, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("a1b2@_1", False),
        ("asf1123@sdfmm41@__asfaSDGAS", False),
        ("asfgSASF@_asf", False),
        ("@D1", False),
        ("asdcSAFA13", False),
        ("saf12sd@__dgaa", False)
    ]
)
def test_check_password(input_password: str, expected_result: bool) -> None:
    assert check_password(input_password) == expected_result

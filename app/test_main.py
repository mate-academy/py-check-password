from app.main import check_password

from pytest import mark


@mark.parametrize(
    "income_pass, exp_result",
    [
        ("Pass@word1", True),
        ("Pass@word@", False),
        ("Ps@wd1", False),
        ("pass@word1", False),
        ("qwerty", False),
        ("Str@ng", False),
        ("", False),
        ("111111111", False),
        ("pAsswordSuper3", False),
        ("More_than@sixteen_S1mbols", False),
    ]
)
def test_check_password(income_pass: str, exp_result: str) -> None:
    assert check_password(income_pass) == exp_result

from app import main


def test_check_only_letters() -> None:
    assert main.check_password("P@ssword") is False


def test_check_least_eight_chars() -> None:
    assert main.check_password("P@s2wo") is False


def test_check_max_chars() -> None:
    assert main.check_password("P@ssw2rdP@ssworda") is False


def test_check_1_digit() -> None:
    assert main.check_password("P@sswordPrda") is False


def test_check_uppercase() -> None:
    assert main.check_password("ds#2worddsa") is False


def test_check_without_spec_symb() -> None:
    assert main.check_password("ds2wWrddsa") is False

from app.main import check_password

import pytest


@pytest.mark.parametrize("inputs, expected",
                         [("Short#1", False),
                          ("gOOd_enough_2", True)])
def test_password_length(inputs: str, expected: bool) -> None:
    assert check_password(inputs) is expected


def test_if_right_signs_are_used() -> None:
    assert check_password("12бвгдеЖЗИ_-") is False
    assert check_password("12беЖewEF_-") is False
    assert check_password("12TobiAsz_-") is True


def test_if_special_signs_are_used() -> None:
    assert check_password("12бghjgS") is False
    assert check_password("1SerimaF") is False
    assert check_password("12TobiAsz_-") is True

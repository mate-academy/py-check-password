from app.main import check_password


def test_password_has_no_upper_letter() -> None:
    assert not check_password("qwert$5iopas")


def test_password_has_no_digit() -> None:
    assert not check_password("qwerT$uiopas")


def test_password_has_no_special() -> None:
    assert not check_password("qwerTy5iopas")


def test_password_has_not_allow_special() -> None:
    assert not check_password("qwerT*5iopas")


def test_password_has_1_digit_1_special_character_1_uppercase_letter() -> None:
    assert check_password("qwerT$5iopas")


def test_password_has_less_than_8_characters() -> None:
    assert not check_password("qwerT$5")


def test_password_has_at_least_8_characters() -> None:
    assert check_password("qwerT$5i")


def test_password_maximum_16_characters_inclusive() -> None:
    assert check_password("qwerT$5iopasdfgh")


def test_password_has_more_than_16_characters() -> None:
    assert not check_password("qwerT$5iopasdfghj")

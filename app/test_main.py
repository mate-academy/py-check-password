from app.main import check_password


def test_not_anyone_upper_case_symbol() -> None:
    assert check_password("ascu#fn2djc") is False


def test_not_anyone_special_symbol() -> None:
    assert check_password("asРufnd1jc") is False


def test_not_anyone_digit() -> None:
    assert check_password("_sРufn##djc") is False


def test_password_count_illegal_letter() -> None:
    assert check_password("_sР4fn#гjc") is False


def test_password_at_least_8_characters() -> None:
    assert check_password("HAo43$gt") is True


def test_password_count_less_8_characters() -> None:
    assert check_password("Ho43$gt") is False


def test_password_count_maximum_16_characters_inclusive() -> None:
    assert check_password("Ho43$gt__1HqT26s") is True


def test_password_count_more_16_characters_inclusive() -> None:
    assert check_password("Ho43$gt_p_1HqT26s") is False

from app.main import check_password


def test_too_short_password() -> None:
    assert check_password("Ab1@f") is False


def test_too_long_password() -> None:
    assert check_password("aAbcdfghklj1@ljmlwswervmllknlknasdvkn") is False


def test_upper_case() -> None:
    assert check_password("abcdf17@dsfff") is False


def test_digits() -> None:
    assert check_password("Fbcdf@dsfff") is False


def test_special() -> None:
    assert check_password("Fbcdfds1fff") is False


def test_correct_password() -> None:
    assert check_password("Fbcdf1567@dsfff") is True

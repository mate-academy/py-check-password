from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "initial_password, expected_res",
    [pytest.param("12Ab!", False, id="required min length"),
     pytest.param("Victory!123@starmamory", False, id="required max length"),
     pytest.param("12345!!!", False, id="required letter in_password"),
     pytest.param("corsica1!", False, id="uppercase letter in_password"),
     pytest.param("World1245", False, id="check special simbols in password"),
     pytest.param("World@@@@", False, id="check digits in password"),
     pytest.param("World@@@^", False, id="check_excessive_in_password")])
def test_required_check_password(initial_password, expected_res):
    check = check_password(initial_password)
    assert check is expected_res

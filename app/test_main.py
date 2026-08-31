import pytest

from app.main import check_password


@pytest.mark.parametrize("password,valid_or_invalid",
                         [
                             pytest.param('Pass@word1', True,
                                          id="Test Good password"),
                             pytest.param('qwertyui', False,
                                          id="Test don't have !@#$ "
                                          "and big later and number"),
                             pytest.param('Str@ngerman', False,
                                          id="Test don't have number"),
                             pytest.param('Strangerman1', False,
                                          id="Test don't have !@$#"),
                             pytest.param('str@ngerman1', False,
                                          id="Test dont have big latter"),
                             pytest.param('StR@12', False,
                                          id="Test too short password"),
                             pytest.param('SuperM@n192587555', False,
                                          id="Test too long password")
                         ]
                         )
def test_check_password(password, valid_or_invalid):
    assert check_password(password) == valid_or_invalid

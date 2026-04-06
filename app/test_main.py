import pytest


from app.main import check_password


@pytest.mark.parametrize("password, is_valid", [
    ("", False),
    ("qwerty1", False),
    ("QWERTY_123456789_#", False),
    ("+qwe`=)(%3", False),
    ("Qwerty1!", True),
    ("Zxc#cxZ!", False),
    ("qwertyuiop", False),
    ("123456789", False),
    ("!#!#!#!#!#!#", False),
    ("1!2!3!4!5!6!7!8", False),
    ("Top1TheBest", False),
    ("BestPassword1!!!", True),
    ("Qwerty12345!", True),
    ("Kefteme554@", True),
    ("Top1top!", True),
    ("Boo123#", False),
])
def test_check_password(password, is_valid):
    assert check_password(password) == is_valid
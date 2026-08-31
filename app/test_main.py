import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Password1", False),
        ("1_B", False),
        ("str@ng12", False),
        ("Putin_Huil0!!!!!!!", False),
        ("Slava_Ukraini", False),
        ("Geroam_Sl@va2", True),
        ("My_peremojemo@23", True)
    ],
    ids=["test1: 'Password1' must be False",
         "test2: '1_B' must be False",
         "test3: 'str@ng12' must be False",
         "test4: 'Putin_Huil0!!!!!!!' must be False",
         "test5: 'Slava_Ukraini' must be False",
         "test6: 'Geroam_Sl@va2' must be True",
         "test7: 'My_peremojemo@228' must be True"]
)
def test_valid_password(password: str, result: bool) -> None:
    assert check_password(password) == result

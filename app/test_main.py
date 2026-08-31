import pytest
from app.main import check_password


@pytest.mark.parametrize("password, answer",
                         [
                             ("Pass@word1", True),
                             ("qwerty", False),
                             ("Str@ng", False),
                             ("Pass@word", False),
                             ("Password1", False),
                             ("Ps@wrd1", False),
                             ("Paaaassssssssss@wwwwwwwwwwwwwwwwwword1", False),
                             ("pass@word1", False),
                         ]
                         )
def test_check_password(password: str,
                        answer: bool,
                        ) -> None:
    assert check_password(password) is answer

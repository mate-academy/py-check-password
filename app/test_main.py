import pytest
from app.main import check_password


@pytest.mark.parametrize("password, result",
                         [
                             ("Pass@word1", True),
                             ("qwerty", False),
                             ("Pass@word1_word2", True),
                             ("H@7elloeverybodyjhjhg", False),
                             ("Qwe@rty1", True),
                             ("Play4game", False),
                             ("ddf!3", False),
                             ("st#tion8", False),
                             ("Pass@word1andsometext", False),
                             ("Pass@word", False),
                             ("Ps@d1", False),
                         ])
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

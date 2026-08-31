import pytest
from app.main import check_password


@pytest.mark.parametrize("password, result",
                         [
                             ("Pass@word1", True),
                             ("qwerty", False),
                             ("Str@ng", False),
                             ("H@7elloeverybodyjhjhg", False),
                             ("Q@qwertyui", False),
                             ("Play4game", False),
                             ("A!3", False),
                             ("st#tion8", False)
                         ])
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result

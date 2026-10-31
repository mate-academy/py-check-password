import pytest
from app.main import check_password


class TestCheckPassword():
    @pytest.mark.parametrize(
        "password,expected",
        [
            pytest.param(
                "Pass@word1", True,
                id="should return True if all requirements are implemented"
            ),
            pytest.param(
                "qwerty", False,
                id="should return False for which is too short, "
                   "and has only lowercase letters"
            ),
            pytest.param(
                "Str@ng", False,
                id=" should return False for password which is "
                   "too short and without digit"
            ),
            pytest.param(
                "Pass@word1Pass@word1Pass@word1", False,
                id=" should return False if password is too long"
            ),
            pytest.param(
                "Pa@2", False,
                id=" should return False if password is too short"
            ),
            pytest.param(
                "pass@word1", False,
                id=" should return False for password "
                   "without uppercase letters"
            ),
            pytest.param(
                "Pass@worddd", False,
                id=" should return False for password without digits"
            ),
            pytest.param(
                "Pass%word1", False,
                id=" should return False for not allowed char %"
            ),
            pytest.param(
                "Pass*word1", False,
                id=" should return False for not allowed char *"
            ),
            pytest.param(
                "Pass^word1", False,
                id=" should return False for not allowed char ^"
            ),
            pytest.param(
                "Pass(word1", False,
                id=" should return False for not allowed char ("
            ),
            pytest.param(
                "Pass)word1", False,
                id=" should return False for not allowed char )"
            ),
            pytest.param(
                "Pass{word1", False,
                id=" should return False for not allowed char {"
            ),
            pytest.param(
                "Pass}word1", False,
                id=" should return False for not allowed char }"
            ),
            pytest.param(
                "Pass[word1", False,
                id=" should return False for not allowed char ["
            ),
            pytest.param(
                "Pass]word1", False,
                id=" should return False for not allowed char ]"
            ),
            pytest.param(
                "Pass/word1", False,
                id=" should return False for not allowed char /"
            ),
            pytest.param(
                "Pass\\word1", False,
                id=" should return False for not allowed char \\"
            ),
            pytest.param(
                "Pass?word1", False,
                id=" should return False for not allowed char ?"
            ),
            pytest.param(
                "Pass.word1", False,
                id=" should return False for not allowed char ."
            ),
            pytest.param(
                "Pass,word1", False,
                id=" should return False for not allowed char ,"
            ),
            pytest.param(
                "Pass<word1", False,
                id=" should return False for not allowed char <"
            ),
            pytest.param(
                "Pass>word1", False,
                id=" should return False for not allowed char >"
            ),
            pytest.param(
                "Pass|word1", False,
                id=" should return False for not allowed char |"
            ),
            pytest.param(
                "Passąword1", False,
                id=" should return False for not allowed char ą"
            ),
            pytest.param(
                "Passćword1", False,
                id=" should return False for not allowed char ć"
            ),
            pytest.param(
                "Passęword1", False,
                id=" should return False for not allowed char ę"
            ),
            pytest.param(
                "Passłword1", False,
                id=" should return False for not allowed char ł"
            ),
            pytest.param(
                "Passśword1", False,
                id=" should return False for not allowed char ś"
            ),
            pytest.param(
                "Passóword1", False,
                id=" should return False for not allowed char ó"
            ),
            pytest.param(
                "Passńword1", False,
                id=" should return False for not allowed char ń"
            ),
            pytest.param(
                "Passźword1", False,
                id=" should return False for not allowed char ż"
            ),
            pytest.param(
                "Passżword1", False,
                id=" should return False for not allowed char ż"
            ),
            pytest.param(
                "PassĄword1", False,
                id=" should return False for not allowed char Ą"
            ),
            pytest.param(
                "PassĆword1", False,
                id=" should return False for not allowed char Ć"
            ),
            pytest.param(
                "PassĘword1", False,
                id=" should return False for not allowed char Ę"
            ),
            pytest.param(
                "PassŁword1", False,
                id=" should return False for not allowed char Ł"
            ),
            pytest.param(
                "PassŚword1", False,
                id=" should return False for not allowed char Ś"
            ),
            pytest.param(
                "PassÓword1", False,
                id=" should return False for not allowed char Ó"
            ),
            pytest.param(
                "PassŃword1", False,
                id=" should return False for not allowed char Ń"
            ),
            pytest.param(
                "PassŹword1", False,
                id=" should return False for not allowed char Ź"
            ),
            pytest.param(
                "PassŻword1", False,
                id=" should return False for not allowed char Ż"
            ),
        ]
    )
    def test_check_password(self, password: str, expected: bool) -> None:
        assert check_password(password) == expected

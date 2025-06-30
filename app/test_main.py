import pytest
from app.main import check_password


@pytest.mark.parametrize("passwords", [
    ["d!33dF"],
    ["Ahkh7@"],
    ["jksbEEE27342847447"],
    ["$cgdafcFcfccf"],
    ["ääJk1213fd!>"],
    ["P12SвданняO@@@D"],
    ["ARESDXG"],
    ["dalnvvk/(76G"],
    ["Gkghbkhb76655"],
    ["Zgsdavacv111"],
    ["sfjhaDD76@вдння"],
    ["njfjzQQQQ@!>"],
    ["njfjzQQQQ@!3243423421134444"],

])
def test_check_invalid_password(passwords: str) -> None:
    assert check_password(*passwords) is False


@pytest.mark.parametrize("valid_passwords", [
    ["d!33dJJeef"],
    ["Ahkh7@wefef"],
    ["jk$sbEEE27342847"],
    ["$cgdafcFcfccf32"],
    ["333Jk1213fd!"],
    ["P12SdvdevO@@@D"],
    ["ARESDX243fgdf!G"],
    ["dalnvvk_76G"],
    ["Gkghbk---hb76655"],
    ["Zgsdavacv111&"],
    ["sfjhaDD76@hbdwh#"],
    ["njfjz2133QQQQ@!"],
])
def test_check_valid_password(valid_passwords: str) -> None:
    assert check_password(*valid_passwords) is True

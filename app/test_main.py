from app.main import check_password


def test_cryptocurrency_action() -> None:
    passwords = [
        ["Pass@word1", True],
        ["Pass@word1123frq", True],
        ["qwerty", False],
        ["Str@ng", False],
        ["Str1ng", False],
        ["Pass@word1123frge", False],
        ["Фшот123456@", False],
        ["Str1ng", False]
    ]
    for (
        mock_get_password,
        expected_result
    ) in passwords:

        assert check_password(mock_get_password) == expected_result

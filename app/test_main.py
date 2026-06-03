import pytest
from app.main import check_password


def test_password_valida_exemplo() -> None:
    assert check_password("Pass@word1") is True
    assert check_password("Abcdefg1!") is True
    assert check_password("12345678aB!") is True


def test_password_invalida_exemplo() -> None:
    assert check_password("qwerty") is False
    assert check_password("Str@ng") is False


def test_condicoes_de_contorno_comprimento() -> None:
    assert check_password("A1!bcdef") is True
    assert check_password("A1!bcde") is False

    # Limite superior
    assert check_password("A1!abcdefghijklm") is True
    assert check_password("A1!abcdefghijklmn") is False


def test_ausencia_de_caracteres_obrigatorios() -> None:
    assert check_password("abcdefg1!") is False
    assert check_password("ABCDEFG1!") is True
    assert check_password("abcdefg1@") is False
    assert check_password("Pass@word") is False
    assert check_password("Password12") is False


def test_caracteres_nao_permitidos() -> None:
    assert check_password("Pass @word1") is False
    assert check_password("Pass%word1") is False
    assert check_password("Pass*word1") is False
    assert check_password("Pass.word1") is False
    assert check_password("Pâss@word1") is False


@pytest.mark.parametrize("senha_valida", [
    "Valid$123",
    "A!1bcdefghijk",
    "1_abcdefG",
    "9876543210aB-",
])
def test_varias_senhas_validas(senha_valida: str) -> None:
    assert check_password(senha_valida) is True

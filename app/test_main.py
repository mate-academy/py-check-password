import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password_input, password_result",
    [("Pass@word1", True),
     ("qwerty", False),
     ("Str@ng", False),
     ("ValidPass@123456", True),  # 16 caracteres, válido
     ("InvalidPass@12345", False),  # 17 caracteres, inválido
     ("ThisIsTooLongPass@1", False),  # 19 caracteres, inválido
     ("nouppercase@1", False),  # Sem letra maiúscula
     ("NOLOWERCASE@1", True),
     # Teste para falta de dígito
     ("NoDigitPass@", False),
     # Teste para falta de caractere especial
     ("NoSpecial123", False),
     # Teste para caractere inválido (ex: '?')
     ("Invalid?Char1", False),
     # Teste para caractere inválido (ex: 'ç')
     ("SenhaComÇ@1", False)]
)
def test_check_password(
    password_input: str, password_result: bool
) -> None:
    result = check_password(password_input)
    assert result == password_result

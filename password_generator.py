import random
import string

def generate_password(
    length=12,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_symbols=True
):
    """
    Gera uma senha segura com base nos parâmetros fornecidos.

    Args:
        length (int): O comprimento desejado da senha. Deve ser maior que 0.
        use_uppercase (bool): Incluir letras maiúsculas (A-Z).
        use_lowercase (bool): Incluir letras minúsculas (a-z).
        use_digits (bool): Incluir dígitos (0-9).
        use_symbols (bool): Incluir símbolos comuns (!@#$%^&*()).

    Returns:
        str: A senha gerada.

    Raises:
        ValueError: Se nenhum tipo de caractere for selecionado ou se o comprimento
                    não for um inteiro positivo.
    """
    if not isinstance(length, int) or length <= 0:
        raise ValueError("O comprimento da senha deve ser um número inteiro positivo.")

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation # Inclui uma variedade de símbolos

    if not characters:
        raise ValueError("Pelo menos um tipo de caractere (maiúsculas, minúsculas, dígitos, símbolos) deve ser selecionado.")

    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    print("Gerador de Senhas Seguras")
    try:
        # Exemplo de uso:
        senha1 = generate_password(length=16, use_symbols=True)
        print(f"Senha de 16 caracteres (com símbolos): {senha1}")

        senha2 = generate_password(length=8, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=False)
        print(f"Senha de 8 caracteres (sem símbolos): {senha2}")

        senha3 = generate_password(length=20, use_uppercase=False, use_digits=True, use_symbols=True)
        print(f"Senha de 20 caracteres (sem minúsculas): {senha3}")
    except ValueError as e:
        print(f"Erro: {e}")
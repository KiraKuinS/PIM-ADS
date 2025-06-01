import hashlib


def gerar_hash(senha):
    """
    Gera o hash SHA-256 de uma senha.
    O hash é uma representação criptográfica da senha, garantindo maior segurança
    ao armazenar senhas no sistema.
    
    Parâmetros:
        senha (str): A senha fornecida pelo usuário.

    Retorna:
        str: O hash SHA-256 da senha.
    """
    return hashlib.sha256(senha.encode()).hexdigest()

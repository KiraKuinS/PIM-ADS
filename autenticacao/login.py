import os
import json
from util.seguranca import gerar_hash

CAMINHO_ARQUIVO = "autenticacao/usuarios.json"

def login():
    """
    Realiza o login do usuário.
    Verifica se o nome de usuário e a senha fornecidos estão corretos.
    """
    print("\n--- LOGIN DE USUÁRIO ---")
    nome_usuario = input("Digite seu nome de usuário: ").strip().lower()
    senha = input("Digite sua senha: ").strip()

    # Verifica se o arquivo de usuários existe
    if not os.path.exists(CAMINHO_ARQUIVO):
        print("Nenhum usuário cadastrado ainda.")
        return None

    try:
        # Carrega os dados dos usuários do arquivo JSON
        with open(CAMINHO_ARQUIVO, 'r', encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
    except Exception:
        print("Erro ao ler os dados de usuário.")
        return None

    # Verifica se o nome de usuário existe
    if nome_usuario not in usuarios:
        print("Usuário não encontrado.")
        return None

    # Recupera a senha hash salva no arquivo
    senha_hash_salva = usuarios[nome_usuario]["senha"]

    # Compara a senha fornecida (convertida para hash) com a senha salva
    if gerar_hash(senha) == senha_hash_salva:
        print(f"\nLogin realizado com sucesso! Bem-vindo(a), {usuarios[nome_usuario]['nome']}.")
        return nome_usuario
    else:
        print("Senha incorreta.")
        return None

# Atualiza todas as senhas para hash (se necessário)
with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
    usuarios = json.load(f)

for usuario in usuarios.values():
    senha_pura = usuario["senha"]
    # Só gera hash se a senha ainda não estiver no formato hash (SHA-256 tem 64 caracteres)
    if len(senha_pura) != 64:
        usuario["senha"] = gerar_hash(senha_pura)

# Salva as alterações no arquivo JSON
with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
    json.dump(usuarios, f, indent=4)
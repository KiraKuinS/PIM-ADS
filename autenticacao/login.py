import os
import json
from util.seguranca import gerar_hash

CAMINHO_ARQUIVO = "autenticacao/usuarios.json"

def login():
    print("\n--- LOGIN DE USUÁRIO ---")
    nome_usuario = input("Digite seu nome de usuário: ").strip().lower()
    senha = input("Digite sua senha: ").strip()

    if not os.path.exists(CAMINHO_ARQUIVO):
        print("Nenhum usuário cadastrado ainda.")
        return None

    try:
        with open(CAMINHO_ARQUIVO, 'r', encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
    except Exception:
        print("Erro ao ler os dados de usuário.")
        return None

    if nome_usuario not in usuarios:
        print("Usuário não encontrado.")
        return None

    senha_hash_salva = usuarios[nome_usuario]["senha"]

    if gerar_hash(senha) == senha_hash_salva:
        print(f"\nLogin realizado com sucesso! Bem-vindo(a), {usuarios[nome_usuario]['nome']}.")
        return nome_usuario
    else:
        print("Senha incorreta.")
        return None

# Atualize todas as senhas para hash
with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
    usuarios = json.load(f)

for usuario in usuarios.values():
    senha_pura = usuario["senha"]
    # Só gera hash se ainda não for hash (tamanho 64 para SHA-256)
    if len(senha_pura) != 64:
        usuario["senha"] = gerar_hash(senha_pura)

with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
    json.dump(usuarios, f, indent=4)
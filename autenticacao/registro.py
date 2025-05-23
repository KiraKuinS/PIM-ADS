import os
import json
from util.seguranca import gerar_hash

CAMINHO_ARQUIVO = "autenticacao/usuarios.json"

def registrar_usuario():
    print("\n=== Registro de Usuário ===")
    
    nome = input("Nome completo: ")
    nome_usuario = input("Nome de usuário (único): ").strip().lower()
    senha = input("Senha: ")
    codigo = input("Digite o código de acesso (ou pressione Enter para aluno): ").strip()

    if not nome_usuario.isalnum():
        print("❌ O nome de usuário deve conter apenas letras e números.")
        return

    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, 'r', encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
    else:
        usuarios = {}

    if nome_usuario in usuarios:
        print("❌ Esse nome de usuário já existe.")
        return

    if codigo == "prof123":
        nivel = "professor"
    elif codigo == "admin123":
        nivel = "admin"
    else:
        nivel = "aluno"

    usuarios[nome_usuario] = {
        "nome": nome,
        "senha": gerar_hash(senha),
        "nivel": nivel
    }

    with open(CAMINHO_ARQUIVO, 'w', encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

    print("✅ Usuário registrado com sucesso!")



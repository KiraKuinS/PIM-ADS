import os
import json
from util.seguranca import gerar_hash

CAMINHO_ARQUIVO = "autenticacao/usuarios.json"

def registrar_usuario():
    """
    Permite o registro de um novo usuário no sistema.
    O usuário pode ser registrado como aluno, professor ou administrador,
    dependendo do código de acesso fornecido.
    """
    print("\n=== Registro de Usuário ===")
    
    # Solicita os dados do novo usuário
    nome = input("Nome completo: ")
    nome_usuario = input("Nome de usuário (único): ").strip().lower()
    senha = input("Senha: ")
    codigo = input("Digite o código de acesso (ou pressione Enter para aluno): ").strip()

    # Valida o nome de usuário
    if not nome_usuario.isalnum():
        print("❌ O nome de usuário deve conter apenas letras e números.")
        return

    # Carrega os dados existentes ou cria um novo dicionário
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, 'r', encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
    else:
        usuarios = {}

    # Verifica se o nome de usuário já está em uso
    if nome_usuario in usuarios:
        print("❌ Esse nome de usuário já existe.")
        return

    # Define o nível de acesso com base no código fornecido
    if codigo == "prof123":
        nivel = "professor"
    elif codigo == "admin123":
        nivel = "admin"
    else:
        nivel = "aluno"

    # Adiciona o novo usuário ao dicionário
    usuarios[nome_usuario] = {
        "nome": nome,
        "senha": gerar_hash(senha),  # Armazena a senha como hash para maior segurança
        "nivel": nivel
    }

    # Salva os dados atualizados no arquivo JSON
    with open(CAMINHO_ARQUIVO, 'w', encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

    print("✅ Usuário registrado com sucesso!")



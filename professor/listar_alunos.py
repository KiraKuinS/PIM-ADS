import json
from util.limpar_tela import limpar_tela, pausar

CAMINHO_ARQUIVO = "autenticacao/usuarios.json"

def listar_alunos():
    """
    Lista todos os alunos cadastrados no sistema.
    Exibe o nome de login e o nome completo de cada aluno.
    """
    limpar_tela()

    # Carrega os dados dos usuários do arquivo JSON
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        usuarios = json.load(f)

    # Filtra apenas os usuários com nível "aluno"
    alunos = [(usuario, dados) for usuario, dados in usuarios.items() if dados.get("nivel") == "aluno"]

    # Exibe a lista de alunos ou uma mensagem caso não haja alunos cadastrados
    if alunos:
        print("\nLista de alunos cadastrados:")
        print("-" * 40)
        for idx, (usuario, dados) in enumerate(alunos, 1):
            print(f"{idx}. Usuário de login: {usuario} | Nome: {dados.get('nome')}")
        print("-" * 40)
    else:
        print("Nenhum aluno cadastrado.")

    # Pausa para que o usuário possa visualizar a lista antes de continuar
    pausar()
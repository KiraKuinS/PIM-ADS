import json
from util.limpar_tela import limpar_tela, pausar

CAMINHO_ARQUIVO = "autenticacao/usuarios.json"

def listar_alunos():
    limpar_tela()
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        usuarios = json.load(f)
    alunos = [(usuario, dados) for usuario, dados in usuarios.items() if dados.get("nivel") == "aluno"]
    if alunos:
        print("\nLista de alunos cadastrados:")
        print("-" * 40)
        for idx, (usuario, dados) in enumerate(alunos, 1):
            print(f"{idx}. Usuário de login: {usuario} | Nome: {dados.get('nome')}")
        print("-" * 40)
    else:
        print("Nenhum aluno cadastrado.")
    pausar()
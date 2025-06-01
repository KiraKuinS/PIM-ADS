import json

CAMINHO_ARQUIVO = "autenticacao/usuarios.json"

def alterar_senha(nome_usuario):
    """
    Permite ao usuário alterar sua senha.
    A nova senha é atualizada no arquivo JSON que armazena os dados dos usuários.
    """
    # Carrega os dados dos usuários do arquivo JSON
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        usuarios = json.load(f)

    # Solicita ao usuário que insira a nova senha
    nova_senha = input("Digite a nova senha: ").strip()

    # Atualiza a senha do usuário no dicionário
    usuarios[nome_usuario]["senha"] = nova_senha

    # Salva as alterações de volta no arquivo JSON
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4)

    print("Senha alterada com sucesso!")
import json

CAMINHO_ARQUIVO = "autenticacao/usuarios.json"

def alterar_senha(nome_usuario):
    with open(CAMINHO_ARQUIVO, "r") as f:
        usuarios = json.load(f)
    nova_senha = input("Digite a nova senha: ")
    usuarios[nome_usuario]["senha"] = nova_senha
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump(usuarios, f, indent=4)
    print("Senha alterada com sucesso!")
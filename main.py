from autenticacao.login import login
from autenticacao.registro import registrar_usuario
from aluno.menu_aluno import menu_aluno
from professor.menu_professor import menu_professor
from admin.menu_admin import menu_admin
import json

CAMINHO_ARQUIVO = "autenticacao/usuarios.json"


def main():
    while True:
        print("\n=== PLATAFORMA DIGITAL SEGURA ===")
        print("1. Registrar")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            registrar_usuario()
        elif opcao == "2":
            usuario_logado = login()
            if usuario_logado:
                with open(CAMINHO_ARQUIVO, 'r', encoding="utf-8") as arquivo:
                    usuarios = json.load(arquivo)
                nivel = usuarios[usuario_logado]["nivel"]
                if nivel == "aluno":
                    menu_aluno(usuario_logado)
                elif nivel == "professor":
                    menu_professor(usuario_logado)
                elif nivel == "admin":
                    menu_admin()
                else:
                    print("Nível de acesso desconhecido.")
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

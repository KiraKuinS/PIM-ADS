from autenticacao.login import login
from autenticacao.registro import registrar_usuario
from aluno.menu_aluno import menu_aluno
from professor.menu_professor import menu_professor
import json
from util.limpar_tela import limpar_tela
import os
import json
from aluno.atividades import mostrar_relatorio_por_materia

CAMINHO_ARQUIVO = "autenticacao/usuarios.json"
PASTA_CONTEUDOS = "atividades"
PASTA_AULAS = "aulas"

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
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

def menu_admin():
    """
    Exibe o menu principal do administrador, permitindo gerenciar usuários,
    visualizar relatórios de alunos e gerenciar conteúdos.
    """
    while True:
        limpar_tela()
        print("=" * 45)
        print("     MENU ADMINISTRADOR".center(45))
        print("=" * 45)
        print(" 1. Ver todos os usuários")
        print(" 2. Visualizar relatórios de alunos")
        print(" 3. Gerenciar conteúdos")
        print(" 4. Sair")
        print("=" * 45)
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            ver_todos_usuarios()
        elif opcao == "2":
            nome_usuario = input("Digite o nome do aluno: ").strip()
            mostrar_relatorio_por_materia(nome_usuario)
        elif opcao == "3":
            gerenciar_conteudos()
        elif opcao == "4":
            print("Saindo do menu administrador...")
            break
        else:
            print("Opção inválida.")
        input("\nPressione Enter para continuar...")

def ver_todos_usuarios():
    """
    Lista todos os usuários cadastrados no sistema, exibindo seus nomes e níveis de acesso.
    """
    limpar_tela()
    if not os.path.exists(CAMINHO_ARQUIVO):
        print("Nenhum usuário encontrado.")
        input("\nPressione Enter para continuar...")
        return
    with open(CAMINHO_ARQUIVO, 'r', encoding="utf-8") as f:
        usuarios = json.load(f)
    print("\n=== Lista de Usuários ===")
    for nome, dados in usuarios.items():
        print(f"Nome: {nome}, Nível: {dados['nivel']}")
    input("\nPressione Enter para continuar...")

def gerenciar_conteudos():
    """
    Permite ao administrador gerenciar os conteúdos disponíveis no sistema.
    Inclui opções para listar, adicionar e remover conteúdos.
    """
    while True:
        limpar_tela()
        print("\n=== Gerenciar Conteúdos ===")
        print("1. Listar conteúdos")
        print("2. Adicionar conteúdo")
        print("3. Remover conteúdo")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            listar_conteudos(PASTA_CONTEUDOS)
        elif opcao == "2":
            adicionar_conteudo(PASTA_CONTEUDOS)
        elif opcao == "3":
            remover_conteudo(PASTA_CONTEUDOS)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        
def listar_conteudos(pasta):
    """
    Lista todos os conteúdos disponíveis em uma pasta específica.
    """
    limpar_tela()
    if not os.path.exists(pasta):
        print("Nenhum conteúdo encontrado.")
        input("\nPressione Enter para continuar...")
        return
    conteudos = [f.replace('.txt', '').replace('.json', '') for f in os.listdir(pasta) if f.endswith('.txt') or f.endswith('.json')]
    if not conteudos:
        print("Nenhum conteúdo disponível.")
        input("\nPressione Enter para continuar...")
        return
    print("\n=== Conteúdos Disponíveis ===")
    for idx, conteudo in enumerate(conteudos, start=1):
        print(f"{idx}. {conteudo.capitalize()}")
    input("\nPressione Enter para continuar...")

def adicionar_conteudo(pasta):
    """
    Adiciona um novo conteúdo ao sistema.
    """
    limpar_tela()
    nome_conteudo = input("Digite o nome do novo conteúdo: ").strip()
    if not nome_conteudo:
        print("Nome inválido.")
        input("\nPressione Enter para continuar...")
        return
    caminho_arquivo = os.path.join(pasta, f"{nome_conteudo}.txt" if pasta == PASTA_AULAS else f"{nome_conteudo}.json")
    if os.path.exists(caminho_arquivo):
        print("Conteúdo já existe.")
        input("\nPressione Enter para continuar...")
        return

    if pasta == PASTA_AULAS:
        # Adiciona uma aula
        limpar_tela()
        print(f"Adicionando conteúdo para a aula: {nome_conteudo}")
        conteudo = input("Digite o conteúdo da aula: ").strip()
        with open(caminho_arquivo, 'w', encoding="utf-8") as f:
            f.write(conteudo)
        print(f"Aula '{nome_conteudo}' adicionada com sucesso!")
    else:
        # Adiciona uma atividade
        questoes = []
        while True:
            limpar_tela()
            print(f"Adicionando perguntas para a atividade: {nome_conteudo}")
            pergunta = input("Digite a pergunta: ").strip()
            alternativas = []
            for i in range(4):  # Supondo 4 alternativas
                alternativa = input(f"Digite a alternativa {i + 1}: ").strip()
                alternativas.append(alternativa)
            resposta_correta = input("Digite o número da alternativa correta (1-4): ").strip()
            questoes.append({
                "pergunta": pergunta,
                "alternativas": alternativas,
                "resposta_correta": resposta_correta
            })
            continuar = input("Deseja adicionar outra pergunta? (s/n): ").strip().lower()
            if continuar != 's':
                break
        with open(caminho_arquivo, 'w', encoding="utf-8") as f:
            json.dump(questoes, f, indent=4)
        print(f"Atividade '{nome_conteudo}' adicionada com sucesso!")
    input("\nPressione Enter para continuar...")

def remover_conteudo(pasta):
    """
    Remove um conteúdo existente do sistema, seja uma atividade ou uma aula.
    """
    limpar_tela()
    listar_conteudos(pasta)
    nome_conteudo = input("Digite o nome do conteúdo a ser removido: ").strip()
    caminho_arquivo = os.path.join(pasta, f"{nome_conteudo}.txt" if pasta == PASTA_AULAS else f"{nome_conteudo}.json")
    if not os.path.exists(caminho_arquivo):
        print("Conteúdo não encontrado.")
        input("\nPressione Enter para continuar...")
        return
    os.remove(caminho_arquivo)
    print(f"Conteúdo '{nome_conteudo}' removido com sucesso!")
    input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
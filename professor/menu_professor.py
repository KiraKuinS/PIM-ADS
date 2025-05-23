from util.limpar_tela import limpar_tela, pausar
from professor.listar_alunos import listar_alunos
from aluno.relatorio import gerar_relatorio_detalhado
import os
import json
import shutil

CAMINHO_ARQUIVO = "autenticacao/usuarios.json"

def menu_professor(nome_professor):
    while True:
        limpar_tela()
        print("=" * 43)
        print("             MENU DO PROFESSOR")
        print("=" * 43)
        print(" 1. Ver relatório de um aluno")
        print(" 2. Listar todos os alunos")
        print(" 3. Lançar nota do aluno")
        print(" 4. Sair")
        print("=" * 43)
        escolha = input("\nDigite o número da opção desejada: ").strip()
        if escolha == "1":
            nome_aluno = input("\nDigite o nome do aluno: ")
            gerar_relatorio_detalhado(nome_aluno)  # Gera o relatório atualizado
            caminho = f"relatorios/relatorios_txt/relatorio_{nome_aluno}.txt"
            if os.path.exists(caminho):
                limpar_tela()
                with open(caminho, "r", encoding="utf-8") as f:
                    print(f.read())
                baixar = input(
                    "\nDeseja baixar o relatório para sua pasta Downloads? (s/n): ").strip().lower()
                if baixar == "s":
                    pasta_downloads = os.path.join(
                        os.path.expanduser("~"), "Downloads")
                    if not os.path.exists(pasta_downloads):
                        print("Pasta de Downloads não encontrada.")
                    else:
                        caminho_destino = os.path.join(
                            pasta_downloads, f"relatorio_{nome_aluno}.txt")
                        shutil.copy2(caminho, caminho_destino)
                        print(f"Relatório copiado para: {caminho_destino}")
            else:
                print("Relatório não encontrado para este aluno.")
            pausar()
        elif escolha == "2":
            listar_alunos()
        elif escolha == "3":
            lancar_nota_professor(nome_professor)
        elif escolha == "4":
            print("Saindo do menu do professor.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            pausar()

def lancar_nota_professor(nome_professor):
    limpar_tela()
    nome_aluno = input("Digite o nome de login do aluno: ").strip()
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        usuarios = json.load(f)
    if nome_aluno not in usuarios or usuarios[nome_aluno].get("nivel") != "aluno":
        print("Aluno não encontrado.")
        pausar()
        return

    try:
        participacao = float(input("Nota de participação (0 a 10): ").replace(',', '.'))
        projeto_final = float(input("Nota do projeto final (0 a 10): ").replace(',', '.'))
        comentario = input("Comentário do professor (opcional): ").strip()
        for nota in [participacao, projeto_final]:
            if nota < 0 or nota > 10:
                print("Notas devem ser entre 0 e 10.")
                pausar()
                return
    except ValueError:
        print("Valor inválido.")
        pausar()
        return

    caminho = f"relatorios/relatorios_txt/nota_{nome_aluno}.json"
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            notas = json.load(f)
    else:
        notas = {}

    notas[nome_professor] = {
        "participacao": participacao,
        "projeto_final": projeto_final,
        "comentario": comentario
    }

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(notas, f, indent=4)
    print("Notas lançadas com sucesso!")

    caminho_projeto = f"relatorios/relatorios_txt/projeto_final_{nome_aluno}.txt"
    if os.path.exists(caminho_projeto):
        print("\n=== Projeto Final do Aluno ===")
        with open(caminho_projeto, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("O aluno ainda não enviou o projeto final.")

    pausar()

def mostrar_notas_professores(nome_usuario):
    caminho_nota = f"relatorios/relatorios_txt/nota_{nome_usuario}.json"
    if os.path.exists(caminho_nota):
        with open(caminho_nota, "r", encoding="utf-8") as f:
            notas = json.load(f)
        print("\nNotas lançadas pelos professores:")
        print("-" * 50)
        for prof, dados in notas.items():
            media = (dados["participacao"] + dados["projeto_final"]) / 2
            situacao = "Aprovado" if media >= 7 else "Em exame"
            print(f"Professor: {prof}")
            print(f"  Participação: {dados['participacao']:.1f}")
            print(f"  Projeto final: {dados['projeto_final']:.1f}")
            print(f"  Média: {media:.1f} | Situação: {situacao}")
            if dados.get("comentario"):
                print(f"  Comentário: {dados['comentario']}")
            print("-" * 50)
    else:
        print("\nNenhuma nota lançada por professores ainda.")
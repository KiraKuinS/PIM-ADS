import os
import shutil
from util.limpar_tela import limpar_tela, pausar

def exibir_conteudos():
    """
    Exibe as matérias disponíveis e permite que o aluno visualize o conteúdo das aulas.
    O aluno pode navegar pelas matérias, selecionar uma aula e, se desejar, baixar o conteúdo.
    """
    pasta = "conteudos"  # Diretório onde as matérias e aulas estão armazenadas
    while True:
        limpar_tela()
        # Lista todas as pastas dentro da pasta "conteudos", que representam as matérias
        materias = [d for d in os.listdir(pasta) if os.path.isdir(os.path.join(pasta, d))]
        if not materias:
            print("Nenhuma matéria disponível.")
            pausar()
            return

        print("\nMatérias disponíveis:")
        for idx, nome in enumerate(materias, 1):
            print(f"{idx}. {nome.capitalize()}")
        print(f"{len(materias)+1}. Voltar ao menu do aluno")

        try:
            opc = int(input("Escolha a matéria: "))
            if opc == len(materias)+1:
                break  # Volta ao menu do aluno
            materia_escolhida = materias[opc-1]
            caminho_materia = os.path.join(pasta, materia_escolhida)

            # Lista todas as aulas disponíveis na matéria selecionada
            aulas = [f for f in os.listdir(caminho_materia) if f.endswith('.txt')]
            if not aulas:
                print("Nenhuma aula disponível para essa matéria.")
                pausar()
                continue

            while True:
                limpar_tela()
                print(f"\nAulas disponíveis em {materia_escolhida.capitalize()}:")
                for idx, nome in enumerate(aulas, 1):
                    print(f"{idx}. {nome.replace('.txt', '').capitalize()}")
                print(f"{len(aulas)+1}. Voltar para as matérias")

                opc_aula = input("\nEscolha a aula para visualizar ou digite o número para voltar: ")
                if not opc_aula.isdigit() or int(opc_aula) < 1 or int(opc_aula) > len(aulas)+1:
                    print("Opção inválida.")
                    pausar()
                    continue
                opc_aula = int(opc_aula)
                if opc_aula == len(aulas)+1:
                    break  # Volta para a lista de matérias

                aula_escolhida = aulas[opc_aula-1]
                caminho_aula = os.path.join(caminho_materia, aula_escolhida)
                limpar_tela()
                print("-"*40)
                print(f"Conteúdo da aula: {aula_escolhida.replace('.txt','').capitalize()}")
                print("-"*40)
                # Exibe o conteúdo da aula
                with open(caminho_aula, "r", encoding="utf-8") as f:
                    print(f.read())
                print("-"*40)

                # Pergunta se o aluno deseja baixar o conteúdo da aula
                baixar = input("Deseja baixar esta aula para sua pasta de Downloads? (s/n): ").strip().lower()
                if baixar == "s":
                    pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
                    if not os.path.exists(pasta_downloads):
                        print("Pasta de Downloads não encontrada.")
                    else:
                        caminho_destino = os.path.join(pasta_downloads, aula_escolhida)
                        shutil.copy2(caminho_aula, caminho_destino)
                        print(f"Aula copiada para: {caminho_destino}")
                pausar()
        except (IndexError, ValueError):
            print("Opção inválida.")
            pausar()

from aluno.conteudo import exibir_conteudos
from aluno.atividades import escolher_e_fazer_atividade
from aluno.relatorio import gerar_relatorio_detalhado
from autenticacao.alterar_senha import alterar_senha
from util.limpar_tela import limpar_tela, pausar
from professor.menu_professor import mostrar_notas_professores
import os
import shutil


def menu_aluno(nome_usuario):
    while True:
        limpar_tela()
        print("=" * 44)
        print("                 MENU ALUNO")
        print("=" * 44)
        print(" 1. Ver conteúdos")
        print(" 2. Fazer atividades")
        print(" 3. Ver relatório detalhado")
        print(" 4. Alterar senha")
        print(" 5. Registrar participação (fórum, dúvida, etc)")
        print(" 6. Enviar projeto final")
        print(" 7. Sair")
        print("=" * 45)
        escolha = input("\nDigite o número da opção desejada: ").strip()

        if escolha == "1":
            exibir_conteudos()
            pausar()
        elif escolha == "2":
            escolher_e_fazer_atividade(nome_usuario)
            gerar_relatorio_detalhado(nome_usuario)
            pausar()
        elif escolha == "3":
            gerar_relatorio_detalhado(nome_usuario)  # Gera o relatório atualizado
            caminho = f"relatorios/relatorios_txt/relatorio_{nome_usuario}.txt"
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
                            pasta_downloads, f"relatorio_{nome_usuario}.txt")
                        shutil.copy2(caminho, caminho_destino)
                        print(f"Relatório copiado para: {caminho_destino}")
            else:
                print("Relatório ainda não foi gerado para este aluno.")
            pausar()
        elif escolha == "4":
            alterar_senha(nome_usuario)
            pausar()
        elif escolha == "5":
            from aluno.participacao import registrar_participacao
            registrar_participacao(nome_usuario)
            pausar()
        elif escolha == "6":
            from aluno.projeto_final import enviar_projeto_final
            enviar_projeto_final(nome_usuario)
            pausar()
        elif escolha == "7":
            confirmar = input(
                "\nTem certeza que deseja sair? (s/n): ").strip().lower()
            if confirmar == "s":
                print("Saindo do menu do aluno.")
                break
            else:
                print("Operação cancelada.")
                pausar()
        else:
            print("Opção inválida. Tente novamente.")
            pausar()

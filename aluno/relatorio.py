import os
import json

def gerar_relatorio_detalhado(nome_usuario):
    caminho = f"relatorios/relatorios_txt/relatorio_{nome_usuario}.txt"
    caminho_nota = f"relatorios/relatorios_txt/nota_{nome_usuario}.json"
    caminho_projeto = f"relatorios/relatorios_txt/projeto_final_{nome_usuario}.txt"
    caminho_respostas = "relatorios/respostas_alunos.json"

    # Lê as atividades do aluno a partir do arquivo compartilhado
    atividades = []
    if os.path.exists(caminho_respostas):
        with open(caminho_respostas, "r", encoding="utf-8") as f_ativ:
            todas = json.load(f_ativ)
            atividades = [a for a in todas if a.get("nome") == str(nome_usuario)]

    with open(caminho, "w", encoding="utf-8") as f:
        f.write("="*60 + "\n")
        f.write(f"{'RELATÓRIO DE DESEMPENHO DO ALUNO: ' + str(nome_usuario):^60}\n")
        f.write("="*60 + "\n\n")

        f.write("| Matéria      |    Data    | Total | Acertos | % Acerto |\n")
        f.write("-"*60 + "\n")
        media_percentual = 0
        if atividades:
            for atividade in atividades:
                materia = atividade.get("conteudo", "-")
                data = atividade.get("data", "-")
                total = atividade.get("total_questoes", 0)
                acertos = atividade.get("acertos", 0)
                percentual = atividade.get("porcentagem", 0)
                media_percentual += percentual
                f.write(f"| {materia:^12} | {data:^10} | {total:^5} | {acertos:^7} | {percentual:^7.1f}% |\n")
            media_percentual /= len(atividades)
        else:
            f.write("|      -       |     -      |   -   |   -     |    -     |\n")
        f.write("-"*60 + "\n\n")
        f.write(f"MÉDIA DE ACERTOS: {media_percentual:.1f}%\n")
        f.write("="*60 + "\n\n")
        f.write(f"{'SEÇÃO: NOTAS DOS PROFESSORES':^60}\n")
        f.write("="*60 + "\n\n")

        if os.path.exists(caminho_nota):
            with open(caminho_nota, "r", encoding="utf-8") as nf:
                notas = json.load(nf)
            for prof, dados in notas.items():
                participacao = dados.get("participacao", 0)
                projetos = dados.get("projetos", 0)
                media = (participacao + projetos) / 2
                situacao = "Aprovado" if media >= 7 else "Em exame"

                f.write(f"Professor: {prof}\n")
                f.write("-"*60 + "\n")
                f.write(f"| Participação: {participacao:<4} | Projetos: {projetos:<4} |\n")
                f.write(f"| Média: {media:<5.1f}        | Situação: {situacao:<18}|\n")
                f.write("-"*60 + "\n")
                if dados.get("comentario"):
                    f.write(f"Comentário: {dados['comentario']}\n")
                f.write("="*60 + "\n\n")
        else:
            f.write("Nenhuma nota lançada por professores ainda.\n")
            f.write("="*60 + "\n\n")

        f.write(f"{'Notas lançadas pelos professores':^60}\n")
        f.write("-"*60 + "\n")
        if os.path.exists(caminho_projeto):
            with open(caminho_projeto, "r", encoding="utf-8") as pf:
                projeto = pf.read().strip()
            if projeto:
                f.write(projeto + "\n")
            else:
                f.write("→ O aluno enviou o projeto final, mas está vazio.\n")
        else:
            f.write("→ O aluno ainda não enviou o projeto final.\n")
        f.write("="*60 + "\n")
if __name__ == "__main__":
    gerar_relatorio_detalhado()
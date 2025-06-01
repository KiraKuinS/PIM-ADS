import json
import os
from datetime import datetime

def registrar_participacao(nome_usuario):
    """
    Registra a participação do aluno em atividades como fóruns, dúvidas ou projetos.
    O registro é salvo em um arquivo JSON específico para o aluno.
    """
    # Define o caminho do arquivo onde as participações serão armazenadas
    caminho = f"relatorios/relatorios_txt/participacao_{nome_usuario}.json"

    # Verifica se o arquivo já existe; caso contrário, cria uma lista vazia
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            participacoes = json.load(f)
    else:
        participacoes = []

    # Solicita ao aluno que descreva o tipo de participação
    tipo = input("Descreva o tipo de participação (ex: Fórum, Dúvida, Projeto): ").strip()

    # Adiciona a nova participação com a data e hora atuais
    participacoes.append({
        "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "tipo": tipo
    })

    # Salva a lista de participações no arquivo JSON
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(participacoes, f, indent=4)

    print("Participação registrada!")
import json
import os
from datetime import datetime

def registrar_participacao(nome_usuario):
    caminho = f"relatorios/relatorios_txt/participacao_{nome_usuario}.json"
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            participacoes = json.load(f)
    else:
        participacoes = []
    tipo = input("Descreva o tipo de participação (ex: Fórum, Dúvida, Projeto): ").strip()
    participacoes.append({
        "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "tipo": tipo
    })
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(participacoes, f, indent=4)
    print("Participação registrada!")
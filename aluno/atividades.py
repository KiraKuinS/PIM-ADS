import json
import os
import datetime

ARQUIVO_RELATORIO = "relatorios/respostas_alunos.json"


def carregar_questoes(conteudo):
    caminho_arquivo = f"atividades/{conteudo}.json"
    if not os.path.exists(caminho_arquivo):
        return []
    with open(caminho_arquivo, 'r', encoding="utf-8") as f:
        return json.load(f)


def carregar_relatorio():
    if not os.path.exists(ARQUIVO_RELATORIO):
        return []
    try:
        with open(ARQUIVO_RELATORIO, 'r', encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def salvar_relatorio(relatorio):
    with open(ARQUIVO_RELATORIO, 'w', encoding="utf-8") as f:
        json.dump(relatorio, f, indent=4)


def mostrar_relatorio_por_materia(nome_usuario):
    relatorio = carregar_relatorio()
    materias = {}
    for atividade in relatorio:
        if atividade.get("nome") == nome_usuario and "conteudo" in atividade:
            materias[atividade["conteudo"]] = atividade["porcentagem"]
    if not materias:
        print("Nenhuma atividade encontrada.")
        return
    print("\n=== Desempenho por matéria ===")
    for materia, porcentagem in materias.items():
        print(f"{materia.capitalize()}: {porcentagem}%")


def salvar_atividades(nome, total_questoes, acertos, conteudo):
    data_hoje = datetime.date.today().isoformat()
    porcentagem = (acertos / total_questoes) * 100 if total_questoes > 0 else 0

    relatorio = carregar_relatorio()

    nova_atividade = {
        "nome": nome,
        "conteudo": conteudo,
        "data": data_hoje,
        "total_questoes": total_questoes,
        "acertos": acertos,
        "porcentagem": round(porcentagem, 1)
    }

    # Atualiza se já existe, senão adiciona novo
    atualizado = False
    for i, atividade in enumerate(relatorio):
        if (
            atividade.get("nome") == nome
            and atividade.get("conteudo") == conteudo
        ):
            relatorio[i] = nova_atividade
            atualizado = True
            break
    if not atualizado:
        relatorio.append(nova_atividade)
    salvar_relatorio(relatorio)
    print("Atividade salva:", nova_atividade)


def fazer_atividades(nome_usuario, conteudo):
    relatorio = carregar_relatorio()
    for atividade in relatorio:
        if atividade.get("nome") == nome_usuario and atividade.get("conteudo") == conteudo:
            print(f"\nVocê já fez essa atividade em {atividade['data']}.")
            return
    questoes = carregar_questoes(conteudo)
    if not questoes:
        print("Nenhuma atividade disponível no momento.")
        return
    print("\n=== Atividade de Múltipla Escolha ===")
    acertos = 0
    for numero_questao, questao in enumerate(questoes, start=1):
        print(f"\n{numero_questao}. {questao['pergunta']}")
        for numero_alternativa, texto_alternativa in enumerate(questao['alternativas'], start=1):
            print(f"   {numero_alternativa}. {texto_alternativa}")
        resposta = input("Sua resposta (número): ").strip()
        correta = str(questao['resposta_correta'])
        if resposta == correta:
            print("✅ Correto!")
            acertos += 1
        else:
            print(f"❌ Errado. Resposta correta: {correta}")
    print(f"\n🎉 Você acertou {acertos} de {len(questoes)} perguntas.")
    salvar_atividades(nome_usuario, len(questoes), acertos, conteudo)


def escolher_e_fazer_atividade(nome_usuario):
    conteudos = [f.replace('.json', '') for f in os.listdir("atividades") if f.endswith('.json')]
    
    if not conteudos:
        print("Nenhum conteúdo disponível.")
        return
    print("\nConteúdos disponíveis:")
    
    for idx, c in enumerate(conteudos, 1):
        print(f"{idx}. {c.capitalize()}")
        
    try:
        opc = int(input("Digite o número do conteúdo desejado: "))
        conteudo_escolhido = conteudos[opc-1]
        fazer_atividades(nome_usuario, conteudo_escolhido)
        
    except (IndexError, ValueError):
        print("Conteúdo inválido.")


def salvar_atividade(nome_usuario, conteudo, data, total_questoes, acertos, porcentagem):
    caminho = f"relatorios/relatorios_txt/atividades_{nome_usuario}.json"
    nova_atividade = {
        "nome": nome_usuario,
        "conteudo": conteudo,
        "data": data,
        "total_questoes": total_questoes,
        "acertos": acertos,
        "porcentagem": porcentagem
    }
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            atividades = json.load(f)
    else:
        atividades = []
    atividades.append(nova_atividade)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(atividades, f, indent=4)

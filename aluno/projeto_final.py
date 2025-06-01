import os

def enviar_projeto_final(nome_usuario):
    """
    Permite ao aluno enviar seu projeto final.
    O projeto pode ser baseado em temas sugeridos ou em um tema livre relacionado ao curso.
    O texto é salvo em um arquivo específico para o aluno.
    """
    print("\n=== Instruções para o Projeto Final ===")
    print("Escolha um dos temas abaixo ou proponha um tema relacionado ao conteúdo estudado:")
    print("1. Desenvolva um pequeno sistema em Python para resolver um problema do seu dia a dia.")
    print("2. Escreva um texto sobre a importância da segurança digital na internet.")
    print("3. Descreva um caso real ou fictício de uso da tecnologia em uma empresa ou escola.")
    print("4. Faça um texto criativo sobre um tema livre relacionado ao curso.")
    print("5. Relate como aplicou algum conceito aprendido na sua vida.")
    print("Digite seu projeto final abaixo (mínimo de 200 caracteres):\n")

    # Recebe o texto do projeto final do aluno
    texto = input()

    # Verifica se o texto tem pelo menos 200 caracteres
    if len(texto.strip()) < 200:
        print("\nO texto do projeto final deve ter pelo menos 200 caracteres. Você digitou", len(texto.strip()), "caracteres.")
        print("Tente novamente e escreva um texto mais completo.")
        return

    # Define o caminho onde o projeto final será salvo
    caminho = f"relatorios/relatorios_txt/projeto_final_{nome_usuario}.txt"

    # Salva o texto do projeto final em um arquivo
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(texto)

    print("Projeto final enviado com sucesso!")
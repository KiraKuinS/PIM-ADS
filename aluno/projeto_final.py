import os

def enviar_projeto_final(nome_usuario):
    print("\n=== Instruções para o Projeto Final ===")
    print("Escolha um dos temas abaixo ou proponha um tema relacionado ao conteúdo estudado:")
    print("1. Desenvolva um pequeno sistema em Python para resolver um problema do seu dia a dia.")
    print("2. Escreva um texto sobre a importância da segurança digital na internet.")
    print("3. Descreva um caso real ou fictício de uso da tecnologia em uma empresa ou escola.")
    print("4. Faça um texto criativo sobre um tema livre relacionado ao curso.")
    print("5. Relate como aplicou algum conceito aprendido na sua vida.")
    print("Digite seu projeto final abaixo (mínimo de 200 caracteres):\n")
    texto = input()
    if len(texto.strip()) < 200:
        print("\nO texto do projeto final deve ter pelo menos 200 caracteres. Você digitou", len(texto.strip()), "caracteres.")
        print("Tente novamente e escreva um texto mais completo.")
        return
    caminho = f"relatorios/relatorios_txt/projeto_final_{nome_usuario}.txt"
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(texto)
    print("Projeto final enviado com sucesso!")
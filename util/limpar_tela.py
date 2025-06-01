import os

def limpar_tela():
    """
    Limpa a tela do terminal para melhorar a visualização.
    Funciona tanto em sistemas Windows quanto em sistemas baseados em Unix (Linux/Mac).
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """
    Pausa a execução do programa até que o usuário pressione Enter.
    Útil para permitir que o usuário leia as informações antes de continuar.
    """
    input("\nPressione Enter para continuar...")
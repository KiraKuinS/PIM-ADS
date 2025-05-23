from util.limpar_tela import limpar_tela

def menu_admin():
    limpar_tela()
    print("=" * 45)
    print("     MENU ADMINISTRADOR".center(45))
    print("=" * 45)
    print(" 1. Ver todos os usuários")
    print(" 2. Adicionar professores")
    print(" 3. Sair")
    print("=" * 45)
    # Implemente as opções do admin conforme desejar
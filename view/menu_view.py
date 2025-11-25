#   BIBLIOTECA UNIVERSITARIA (view)

from view.autor_view import AutorView
from view.livro_view import LivroView

class MenuView:
    def __init__(self):
        self.autor_view = AutorView()
        self.livro_view = LivroView()

    def exibir_menu(self):
        while True:
            print("\n===== MENU PRINCIPAL =====")
            print("1 - Gerenciar autor")
            print("2 - Gerenciar livro")
            print("3 - Sair")
            op = input("Escolha uma opção: ")

            if op == "1":
                self.autor_view.menu_autor()
            
            elif op == "2":
                self.livro_view.menu_livro()

            elif op == "3":
                print("Encerrando o programa da Biblioteca. . .")
                break

            else:
                print("Opcao inválida! Tente novamente.")
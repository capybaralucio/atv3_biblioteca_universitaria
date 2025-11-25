#   BIBLIOTECA UNIVERSITARIA (view do livro)

from controller.livro_controller import LivroController

class LivroView:
    def menu_livro(self):
        controller = LivroController()

        while True:
            print("\n---- GERENCIAR LIVRO ----\n")
            print("1 - Cadastrar livro")
            print("2 - Listar livro")
            print("3 - Atualizar livro")
            print("4 - Excluir livro")
            print("5 - Voltar ao menu principal")

        
            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                titulo = input("Título: ")
                ano = input("Ano e publicacão: ")
                id_autor = input("ID do autor: ")

                print(controller.cadastrar_livro(titulo, ano, id_autor))

            elif opcao == "2":
                livros = controller.listar_livros()

                if isinstance(livros, str):
                    print(livros)
                    continue

                print("\n=== LISTA DE LIVROS ===")
                for l in livros:
                    print(f"ID: {l[0]} | Título: {l[1]} | Ano: {l[2]} | Autor: {l[3]}")

            elif opcao == "3":
                id_livro = input("ID do livro: ")

                print("\nDigite os novos valores (ou deixe vazio para não mudar):")

                novo_titulo = input("Novo título: ") or None
                novo_ano = input("Novo ano: ") or None
                novo_autor = input("Novo ID do autor: ") or None

                print(controller.atualizar_livro(id_livro, novo_titulo, novo_ano, novo_autor))                

            elif opcao == "4":
                id_livro = input("ID do livro: ")
                print(controller.excluir_livro(id_livro))    

            elif opcao == "5":
                break

            else:
                print ("Opcão inválida. Tente novamente.")
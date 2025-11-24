#   BIBLIOTECA UNIVERSITARIA (controller do livro)

from model.livro_model import LivroModel


class LivroController:
    def __init__(self):
        self.model = LivroModel()


    def cadastrar_livro(self, titulo, ano_publicacao, id_autor):
        if not titulo:
            return "\nO título não pode ser nulo.\n"
        
        if not ano_publicacao:
            return "\nO ano de publicação não pode ser nulo.\n"
        
        if not id_autor:
            return "\nO ID do autor não pode ser nulo.\n"
        
        self.model.cadastrar_livro(titulo, ano_publicacao, id_autor)
        return "\nSeu livro foi cadastrado com sucesso!!\n"
    

    def atualizar_livro(self, id_livro, novo_titulo=None,novo_ano=None, novo_autor=None):
        if not id_livro:
            return "\nID inválido.\n"
        
        if novo_titulo is None and novo_ano is None and novo_autor is None:
            return "\nNada para atualizar.\n"
        
        self.model.atualizar_livro(id_livro, novo_titulo, novo_ano, novo_autor)
        return "\nLivro atualizado com sucesso!!\n"
    

    def excluir_livro(self, id_livro):
        if not id_livro:
            return "\nID inválido.\n"
        
        try:
            self.model.excluir_livro(id_livro)
            return "\nLivro excluído com sucesso!!\n"
        except Exception as e:
            return f"\nErro ao excluir o livro: {e}\n"
        

    def listar_livros(self):
        livros = self.model.listar_livros()

        if not livros:
            return "\nNenhum livro foi encontrado.\n"
        

        texto = "\n----LISTA DE LIVROS----\n"
        for livro in livros:
            texto += f"ID: {livro[0]} | Título: {livro[1]} | Ano: {livro[2]} | Autor: {livro[3]} | Nacionalidade: {livro[4]}\n"
        
        return texto 
#   BIBLIOTECA UNIVERSITARIA (controller do autor)

from model.autor_model import AutorModel


class AutorController:
    def __init__(self):
        self.model = AutorModel()


    def cadastrar_autor(self, nome, nacionalidade):
        if not nome:
            return "\nO nome do autor não pode ser nulo.\n"

        sucesso = self.model.cadastrar_autor(nome, nacionalidade)

        if sucesso:    
            return "\nAutor cadastrado com sucesso!!\n"
        else:
            return "\nErro ao cadastrar autor.\n"


    def listar_autores(self):
        autores = self.model.listar_autores()
        return autores
    

    def atualizar_autor(self, id_autor, novo_nome=None, nova_nacionalidade=None):
        if not str(id_autor).isdigit():
            return "\nID inválido.\n"

        if novo_nome is None and nova_nacionalidade is None:
            return "\nNada para atualizar.\n"

        sucesso = self.model.atualizar_autor(id_autor, novo_nome, nova_nacionalidade)
        
        if sucesso:
            return "\nAutor atualizado com sucesso!!\n"
        else:
            return "\nErro ao atualizar o autor.\n"

    def excluir_autor(self, id_autor):
        if not str(id_autor).isdigit():
            return "\nID inválido.\n"
        
        sucesso = self.model.excluir_autor(id_autor)

        if sucesso:
            return "\nAutor excluído com sucesso!!\n"
        else:
            return f"\nAutor não encontrado ou erro ao excluir.\n"
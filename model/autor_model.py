#   BIBLIOTECA UNIVERSITARIA (model do autor)
from model.conexao import Conexao

class AutorModel:
    def __init__(self):
        try:
            self.conexao = Conexao().conectar()
            self.cursor = self.conexao.cursor()
        except Exception as e:
            print("\nErro ao conectar ao banco:\n", e)


    def cadastrar_autor(self, nome, nacionalidade):
        try:
            sql = "INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s)"
            self.cursor.execute(sql, (nome, nacionalidade))
            self.conexao.commit()
            return True

        except Exception as e:
            print("\nErro ao cadastrar autor:\n", e)
            self.conexao.rollback()
            return False

    def listar_autores(self):
        try:
            self.cursor.execute("SELECT * FROM autor ORDER BY id")
            return self.cursor.fetchall()
        
        except Exception as e:
            print("\nErro ao listar autores.\n", e)
            return[]
       

    def atualizar_autor(self, id_autor, novo_nome=None, nova_nacionalidade=None):
        try:
            sql = "UPDATE autor SET "
            valores = []
            partes = []


            if novo_nome is not None:
                partes.append("nome = %s")
                valores.append(novo_nome)

            if nova_nacionalidade is not None:
                partes.append("nacionalidade = %s")
                valores.append(nova_nacionalidade)

            
            if not partes:
                return False
            

            sql += ", ".join(partes) + " WHERE id = %s"
            valores.append(id_autor)


            self.cursor.execute(sql, tuple(valores))
            self.conexao.commit()
            return self.cursor.rowcount > 0

        except Exception as e:
            print("\nErro ao atualizar o autor.\n", e)
            self.conexao.rollback()
            return False

    def excluir_autor(self, id_autor):
        try:
            sql = "DELETE FROM autor WHERE id=%s"
            self.cursor.execute(sql, (id_autor,))
            self.conexao.commit()
            return self.cursor.rowcount > 0

        except Exception as e:
            print("\nErro ao excluir autor.\n", e)
            self.conexao.rollback()
            return False
    
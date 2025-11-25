#   BIBLIOTECA UNIVERSITARIA (model do livro)
from model.conexao import Conexao

class LivroModel:
    def __init__(self):
        try:
            self.conexao = Conexao().conectar()
            self.cursor = self.conexao.cursor()
        except Exception as e:
            print("\nErro ao conectar ao banco:\n", e)


    def cadastrar_livro(self, titulo, ano_publicacao, id_autor):
        try:
            sql = "INSERT INTO livro (titulo, ano_publicacao, id_autor) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (titulo, ano_publicacao, id_autor))
            self.conexao.commit()
            return True

        except Exception as e:
            print("\nErro ao cadastrar livro.\n", e)
            self.conexao.rollback()
            return False

    def listar_livros(self):
        try:
            sql = """
            SELECT
                livro.id,
                livro.titulo,
                livro.ano_publicacao,
                autor.nome AS nome_autor,
                autor.nacionalidade
            FROM livro
            JOIN autor ON livro.id_autor = autor.id
            ORDER BY livro.id;
            """

            self.cursor.execute(sql)
            return self.cursor.fetchall()
        
        except Exception as e:
            print("\nErro ao listar livros.\n", e)
            return []
        

    def atualizar_livro(self, id_livro, novo_titulo=None, novo_ano=None, novo_autor=None):
        try:
            sql = "UPDATE livro SET "
            valores = []
            partes = []

            if novo_titulo is not None:
                partes.append("titulo = %s")
                valores.append(novo_titulo)

            if novo_ano is not None:
                partes.append("ano_publicacao = %s")
                valores.append(novo_ano)

            if novo_autor is not None:
                partes.append("id_autor = %s")
                valores.append(novo_autor)


            if not partes:
                return False


            sql += ", ".join(partes) + " WHERE id = %s"
            valores.append(id_livro)


            self.cursor.execute(sql, tuple(valores))
            self.conexao.commit()
            return self.cursor.rowcount > 0

        except Exception as e:
            print("\nErro ao atualizar livro.\n", e)
            self.conexao.rollback()
            return False


    def excluir_livro(self, id_livro):
        try:
            sql = "DELETE FROM livro WHERE id = %s"
            self.cursor.execute(sql, (id_livro,))
            self.conexao.commit()
            return self.cursor.rowcount > 0
            
        except Exception as e:
            print("\nErro ao excluir livro.\n", e)
            self.conexao.rollback()
            return False
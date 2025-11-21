#   BIBLIOTECA UNIVERSITARIA (model do livro)
import psycopg2

class LivroModel:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host = "localhost",
                database = "bibliotecabd",
                user = "postgres",
                password = "admin6",
                port = "5432"
            )
            self.cursor = self.conexao.cursor()
            
        except Exception as e:
            print("\nErro ao conectar ao banco:\n", e)


    def cadastrar_livro(self, titulo, ano_publicacao, id_autor):
        try:
            sql = "INSERT INTO livro (titulo, ano_publicacao, id_autor) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (titulo, ano_publicacao, id_autor))
            self.conexao.commit()
            print("\nLivro cadastrado com sucesso!\n")

        except Exception as e:
            print("\nErro ao cadastrar livro.\n", e)
            self.conexao.rollback()


    def listar_livros(self):
        try:
            sql = """
            SELECT
                livro.id,
                livro.titulo,
                livro.ano_publicacao,
                autor.nome AS nome_autor,
                autor.nacionalidade
            FROM LIVRO
            JOIN autor ON livro.id_autor = autor.id;"""

            self.cursor.execute(sql)
            return self.cursor.fetchall()
        
        except Exception as e:
            print("\nErro ao listar livros.\n", e)
            return[]
        

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
                print("\nNenhum campo para atualizar.\n")
                return


            sql += ", ".join(partes) + " WHERE id = %s"
            valores.append(id_livro)


            self.cursor.execute(sql, tuple(valores))
            self.conexao.commit()
            print("\nLivro atualizado com sucesso!\n")

        except Exception as e:
            print("\nErro ao atualizar livro.\n", e)
            self.conexao.rollback()


    def excluir_livro(self, id_livro):
        try:
            sql = "DELETE FROM livro WHERE id=%s"
            self.cursor.execute(sql, (id_livro,))
            self.conexao.commit()
            print("\nLivro excluído com sucesso!\n")

        except Exception as e:
            print("\nErro ao excluir livro.\n", e)
            self.conexao.rollback()


    def fechar_conexao(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
import psycopg2

class Conexao:
    def __init__(self):
        # configure conforme seu banco PostgreSQL
        self.host = "localhost"
        self.database = "biblioteca_uni_av3"
        self.user = "postgres"
        self.password = "admin"

        self.conexao = None

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            return self.conexao
        except Exception as e:
            print("\nErro ao conectar ao banco PostgreSQL:", e)
            return None

    def fechar_conexao(self):
        try:
            if self.conexao:
                self.conexao.close()
        except Exception as e:
            print("Erro ao fechar a conexão:", e)
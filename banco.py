import psycopg2
from psycopg2 import sql

# Conecte-se ao PostgreSQL
conexao = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="191069"
)

# Crie um cursor
cursor = conexao.cursor()

# Nome do banco de dados e da tabela
nome_banco = "usuarios"
nome_tabela = "usuario"

# Crie o banco de dados
cursor.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier(nome_banco)))

# Conecte-se ao novo banco de dados
conexao = psycopg2.connect(
    host="localhost",
    database=nome_banco,
    user="postgres",
    password="191069"
)

# Crie um novo cursor
cursor = conexao.cursor()

# Crie a tabela
cursor.execute(sql.SQL("""
    CREATE TABLE {} (
        id SERIAL PRIMARY KEY auto_increment,
        nome VARCHAR(100),
        email VARCHAR(100),
        senha VARCHAR(100),
        telefone VARCHAR(20),
        data_nascimento DATE,
        genero VARCHAR(20),
        endereco_rua VARCHAR(100),
        endereco_rua2 VARCHAR(100),
        pais VARCHAR(50),
        cidade VARCHAR(50),
        regiao VARCHAR(50),
        cep VARCHAR(20),
        senha VARCHAR(100)
    );
""").format(sql.Identifier(nome_tabela)))

# Feche o cursor e a conexão
cursor.close()
conexao.close()
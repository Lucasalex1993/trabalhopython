from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)  # Ativar CORS para todas as rotas

@app.route('/api/dados', methods=['GET'])
def obter_dados():
    try:
        # Configuração da conexão com o banco de dados
        conexao_banco = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="191069",
            database="usuarios"
        )

        with conexao_banco:
            with conexao_banco.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario")
                resultados = cursor.fetchall()

                # Converter os resultados em um formato que possa ser convertido em JSON
                resultados_formatados = [dict((cursor.description[i][0], valor) for i, valor in enumerate(linha)) for linha in resultados]

        return jsonify(resultados_formatados)

    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

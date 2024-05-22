from . import app
from flask import request, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrar_usuario():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    telefone = request.form['telefone']
    data_nascimento = request.form['data_nascimento']
    genero = request.form['genero']
    endereco_rua = request.form['endereco_rua']
    endereco_rua2 = request.form['endereco_rua2']
    pais = request.form['pais']
    cidade = request.form['cidade']
    regiao = request.form['regiao']
    cep = request.form['cep']
from flask import Flask, render_template, redirect, request, flash, send_from_directory
import os
from pathlib import Path
import psycopg2

caminho = Path(__file__)
pasta_atual = caminho.parent

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TOCHIU'

logado = False

@app.route('/')
def home():
    global logado
    logado = False
    return render_template('login.html')

@app.route('/adm')
def adm():
    if logado == True:
        conect_BD = psycopg2.connect(host='localhost', database='usuarios',user='postgres', password='191069')
    
        if conect_BD is not None:
            print('conectado')
            cursur = conect_BD.cursor()
            cursur.execute('select * from usuario;')
            usuarios = cursur.fetchall()
        return render_template("admin.html",usuarios=usuarios)
    if logado == False:
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    global logado
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    conect_BD = psycopg2.connect(host='localhost', database='usuarios',user='postgres', password='191069')
    cont = 0
    if conect_BD is not None:
        print('conectado')
        cursur = conect_BD.cursor()
        cursur.execute('select * from usuario;')
        usuariosBD = cursur.fetchall()

        for usuario in usuariosBD:
            cont += 1
            usuarioNome = str(usuario[1])
            usuarioSenha = str(usuario[2])

            if nome == 'adm' and senha == '000':
                logado = True
                return redirect('/adm')

            if usuarioNome == nome and usuarioSenha == senha:
                logado = True
                return render_template('/usuario.html',)
              
            
            if cont >= len(usuariosBD):
                flash('USUARIO INVALIDO')
                return redirect("/")
    else:
        return redirect('/')

@app.route('/cadastrarUsuario', methods=['POST'])

def cadastrarUsuario():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    telefone = request.form.get('telefone')
    data_nascimento = request.form.get('data_nascimento')
    genero = request.form.get('genero')
    endereco_rua = request.form.get('endereco_rua')
    endereco_rua2 = request.form.get('endereco_rua2')
    pais = request.form.get('pais')
    cidade = request.form.get('cidade')
    regiao = request.form.get('regiao')
    cep = request.form.get('cep')

    conect_BD = psycopg2.connect(host='localhost', database='usuarios',user='postgres', password='191069')

    if conect_BD is not None:
        cursur = conect_BD.cursor()
        cursur.execute(f"""
            INSERT INTO usuario 
            (nome, email, senha, telefone, data_nascimento, genero, endereco_rua, endereco_rua2, pais, cidade, regiao, cep) 
            VALUES 
            ('{nome}', '{email}', '{senha}', '{telefone}', '{data_nascimento}', '{genero}', '{endereco_rua}', '{endereco_rua2}', '{pais}', '{cidade}', '{regiao}', '{cep}');
        """)
        conect_BD.commit()
        cursur.close()
        conect_BD.close()

    flash(F'{nome} CADASTRADO!!')
    return redirect('/adm')


@app.route('/excluirUsuario', methods=['POST'])
def excluirUsuario():
    global logado
    logado = True
    nome = request.form.get('nome')
    usuarioID = request.form.get('usuarioPexcluir')
    conect_BD = psycopg2.connect(host='localhost', database='usuarios',user='postgres', password='191069')

    if conect_BD is not None:
        cursur = conect_BD.cursor()
        cursur.execute(f"delete from usuario where id='{usuarioID}'; ")
        conect_BD.commit()
        cursur.close()
        conect_BD.close()

    flash(F'{nome} EXCLUIDO')
    return redirect('/adm')


@app.route("/upload", methods=['POST'])
def upload():
    global logado
    logado = True
    
    arquivo = request.files.get('documento')
    nome_arquivo = arquivo.filename.replace(" ","-")
    arquivo.save(os.path.join(f'{pasta_atual}/arquivos/', nome_arquivo))

    flash('Arquivo salvo')
    return redirect('/adm')



@app.route('/download', methods=['POST'])
def download():
    nomeArquivo = request.form.get('arquivosParaDownload')

    return send_from_directory('arquivos', nomeArquivo, as_attachment=True)




if __name__ in "__main__":
    app.run(debug=True)

from . import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    genero = db.Column(db.String(20), nullable=False)
    endereco_rua = db.Column(db.String(120), nullable=False)
    endereco_rua2 = db.Column(db.String(120), nullable=False)
    pais = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    regiao = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'